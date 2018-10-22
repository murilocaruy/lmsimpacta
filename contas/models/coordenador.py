from django.db import models
from django.conf import settings

class Coordenador(models.Model):

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

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'
        db_table = 'COORDENADOR'