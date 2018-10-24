from django.db import models

TIPOS = (
    ('TECNICO', 'Técnico'),
    ('GRADUACAO', 'Graduação'),
    ('PGRADUACAO', 'Pós-Graduação')
)

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=120
    )

    sigla = models.CharField(
        "Sigla",
        max_length=5,
        unique=True
    )

    tipo = models.CharField(
        "Tipo",
        max_length=30,
        choices = TIPOS
    )

    class Meta:
        db_table = 'CURSO'
