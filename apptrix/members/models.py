from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    GENDER_CHOICES = (('М', 'Мужской'), ('Ж', 'Женский'))
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    gender = models.CharField(verbose_name='Пол', choices=GENDER_CHOICES, max_length=7)
    photo = models.ImageField(upload_to='profile_photo/%y/%m/%d/', verbose_name='Фото',
                              default='profile_photo/default_profile_photo.png')

    def __str__(self):
        return self.username


