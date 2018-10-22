from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

TIPOS_USUARIOS = (
    ('C', 'Coordenador'),
    ('A', 'Aluno'),
    ('P', 'Professor')
)

class UsusarioManager(UserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('perfil', 'C')
        return self._create_user(username, password, **extra_fields)

class Usuario(AbstractBaseUser):

    username = models.CharField(
        'Usuário', 
        max_length=30, 
        unique=True,
        db_column='login' 
    )
    password = models.CharField(
        'Senha', 
        max_length=128,
        db_column='senha'
    )
    data_expiracao = models.DateField(
        'Data Expiração', 
        null=True,
        db_column='dtexpiracao'
    )
    perfil = models.CharField(
        'Perfil',
        max_length=1,
        choices=TIPOS_USUARIOS
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UsusarioManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.perfil == 'C'
    
    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.perfil == 'C'

    class Meta:
        verbose_name = 'Usuário',
        verbose_name_plural = 'Usuários'
        db_table = 'USUARIO'
