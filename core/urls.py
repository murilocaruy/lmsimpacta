from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, contato

app_name = "core"

urlpatterns = [
    path("", index, name="home"),
    path('contato/', contato, name="contato"),
    path('entrar/', LoginView.as_view(template_name='entrar.html'), name="entrar"),
    path('sair/', LogoutView.as_view(), name="sair")
]