from django.db import models
from django.conf import settings

class Aluno(models.Model):

    nome = models.CharField(
        'Nome',
        max_length=120
    )

    email = models.EmailField(
        'Email',
        unique=True
    )

    celular = models.CharField(
        'Celular',
        max_length=11,
        unique=True
    )

    ra = models.CharField(
        'RA',
        max_length=7,
        unique=True
    )

    foto = models.ImageField(
        'Foto',
        null=True
    )

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        db_table = 'ALUNO'