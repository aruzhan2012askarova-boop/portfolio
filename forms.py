from django import forms
from .models import Article, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User      
        fields = ['name'] 
        widgets = {
            
            'name': forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter your name!'})
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'content']  
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Заголовок статьи'}),
            'content': forms.Textarea(attrs={"class": 'form-control', 'placeholder': 'Текст статьи...'}),
        }