from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):

    STATUS_CHOICES = [
        ('Online','Online'),
        ('Offline','Offline')
    ]

    username = models.CharField('Username',max_length=255)
    phone = models.CharField('Phone', max_length=20,null=True,blank=True)
    password = models.CharField('Password',max_length=255)
    email = models.EmailField('Email address', unique=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=255,default='Offline')
    last_login = None
    groups = None
    first_name = None
    last_name = None
    date_joined = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    objects = UserManager()

    def __str__(self):
        return self.email