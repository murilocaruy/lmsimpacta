from django.urls import path

from curriculo import views

urlpatterns = [
    path('<str:sigla>/', views.curso, name="curso"),
    path('/<str:abrev>/', views.disciplina, name="disciplina"),
]