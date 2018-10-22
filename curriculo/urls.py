from django.urls import path

from .views import curso

app_name = 'curriculo'
urlpatterns = [
    path('<str:sigla>/', curso, name='curso'),
]