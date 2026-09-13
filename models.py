from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    is_guest = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100,default="No title")

    def __str__(self):
     return f'{self.user.name}: {self.content[:30]}'