from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models

# Create your models here.
from django.db.models.fields.files import ImageFieldFile


class User(AbstractUser):
    avatar: ImageFieldFile = models.ImageField(upload_to='images/profile',verbose_name='تصویر آواتار', null=True, blank=True)
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه' , null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاریر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email