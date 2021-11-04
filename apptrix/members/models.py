import jwt

from datetime import datetime, timedelta

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin

from apptrix import settings


class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Поле email не должно быть пустым.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if email is None:
            raise TypeError('Поле email не должно быть пустым.')
        if password is None:
            raise TypeError('Поле password не должно быть пустым')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Member(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    GENDER_CHOICES = (('М', 'Мужской'), ('Ж', 'Женский'))

    email = models.EmailField(verbose_name='Email', unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=128)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    gender = models.CharField(verbose_name='Пол', choices=GENDER_CHOICES, max_length=7)
    photo = models.ImageField(upload_to='profile_photo/%y/%m/%d/', verbose_name='Фото',
                              default='profile_photo/default_profile_photo.png', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MemberManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

