from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Article
from .forms import ArticleForm, UserForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            user, created = User.objects.get_or_create(name=name)
            request.session["user_id"] = user.id
            return redirect("statia")
    else:
        form = UserForm()
    return render(request, "register.html", {"form": form})

def guest_login(request):
    """Вход под гостевым аккаунтом"""
    guest_user, guest_login = User.objects.get_or_create(
        name="Гость", 
        defaults={"is_guest": True}  
    )
    request.session["user_id"] = guest_user.id
    messages.info(request, "Вы вошли как гость. Вы можете только читать статьи.")
    return redirect("statia")

def statia(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("register")

    user = get_object_or_404(User, id=user_id)
    articles = Article.objects.all().order_by("-timestamp")

    if request.method == "POST":
        if getattr(user, 'is_guest', False):
            messages.error(request, "Гости не могут создавать, изменять или удалять статьи!")
            return redirect("statia")

        if "edit_article_id" in request.POST:
            article_id = request.POST["edit_article_id"]
            article_obj = get_object_or_404(Article, id=article_id)
            
            if article_obj.user == user:
                form = ArticleForm(request.POST, instance=article_obj)
                if form.is_valid():
                    form.save()
                    messages.info(request, "Статья успешно обновлена!")
                    return redirect("statia")

        elif "delete_article_id" in request.POST:
            article_id = request.POST["delete_article_id"]
            article_obj = get_object_or_404(Article, id=article_id)
            if article_obj.user == user:
                request.session["last_deleted_text"] = article_obj.content
                article_obj.delete()
                messages.warning(request, "Статья удалена.")
                return redirect("statia")

        else:
            form = ArticleForm(request.POST)
            if form.is_valid():
                article_obj = form.save(commit=False)
                article_obj.user = user
                article_obj.save()
                messages.success(request, "Статья опубликована!")
                return redirect("statia")
    else:
        form = ArticleForm()

    return render(
        request,
        "statia.html",
        {"articles": articles, "form": form, "current_user": user},
    )

def undo_delete(request):
    """Восстановление последнего удаленного сообщения"""
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("register")
        
    user = get_object_or_404(User, id=user_id)
    
    if getattr(user, 'is_guest', False):
        messages.error(request, "Гости не могут восстанавливать статьи!")
        return redirect("statia")

    deleted_text = request.session.pop("last_deleted_text", None)

    if deleted_text:
        Article.objects.create(user=user, content=deleted_text)
        messages.success(request, "Удаленное сообщение восстановлено!")

    return redirect("statia")