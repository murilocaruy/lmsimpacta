from django.urls import path

from core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name="home" ),
    path('contact/', views.contato, name="contato"),
    path('login/', views.login, name="login")
]