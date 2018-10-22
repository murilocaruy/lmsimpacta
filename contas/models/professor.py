from django.db import models
from django.conf import settings

class Professor(models.Model):

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

    apelido = models.CharField(
        'APELIDO',
        max_length=50
    )

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        db_table = 'PROFESSOR'