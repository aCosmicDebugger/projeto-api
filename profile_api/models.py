from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """ Gerente para os perfis de usuário """

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Usuários devem ter um endereço de email.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """  Cria e salva um superusuário
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo de database para usuários no sistema.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_nome_completo(self):
        """ retorna o nome completo do usuário
        """
        return self.name

    def get_nome_abrv(self):
        """ retorna apenas o primeiro nome do usuário
        """
        return self.name

    def __str__(self):
        """ retorna uma string que respresenta o usuário
        """
        return self.email


class ProfileFeedItem(models.Model):
    """ Atualza o status do perfil
    """

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Retorna o modelo da string
        """
        return self.status_text
