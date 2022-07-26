from email.policy import default
from pydoc import describe
from turtle import title
from django.db import models

from users.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    descriptions = models.TextField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'
    
    