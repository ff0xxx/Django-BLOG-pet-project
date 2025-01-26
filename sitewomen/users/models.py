from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото профиля')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
