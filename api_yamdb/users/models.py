from django.contrib.auth.models import AbstractUser
from django.db import models

USER = "user"
ADMIN = "admin"
MODERATOR = "moderator"

CHOICES = (
    (USER, "user"),
    (ADMIN, "admin"),
    (MODERATOR, "moderator"),
)


class User(AbstractUser):
    username = models.CharField(
        max_length=150, unique=True, blank=False, null=False
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=254,
        unique=True,
        blank=False,
        null=False,
    )
    role = models.CharField(
        "Роль", max_length=10, choices=CHOICES, default=USER, blank=True
    )
    bio = models.TextField(
        "Биография",
        blank=True,
    )
    first_name = models.CharField(
        "Имя пользователя", max_length=150, blank=True
    )
    last_name = models.CharField(
        "Фамилия пользователя", max_length=150, blank=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.is_superuser is True or self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR
