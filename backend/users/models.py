from django.contrib.auth.models import AbstractUser
from django.db import models


class GourmetUser(AbstractUser):
    """Модель Пользователя-гурмана.
    Связана с собой для подписок через M2M."""
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Логин'
    )
    first_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Адрес электронной почты'
    )
    follow = models.ManyToManyField(
        verbose_name='Подписка',
        related_name='followers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
