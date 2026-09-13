from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("statia/", views.statia, name="statia"),
    path('undo/', views.undo_delete, name='undo_delete'),
    path('guest/', views.guest_login, name='guest_login'),  
]