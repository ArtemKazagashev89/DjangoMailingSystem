from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone number")
    avatar = models.ImageField(
        upload_to="avatars/", default="avatars/default_avatar.jpg", blank=True, null=True, verbose_name="Avatar"
    )
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Country")

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name="Token")
    password_reset_token = models.CharField(max_length=100, blank=True, null=True, verbose_name="Password Reset Token")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["email"]
        permissions = [("can_block_user", "Может заблокировать пользователя")]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
