from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token

#Create your models here.



class User(AbstractUser):
    """
    User model to store user data
    """
    # name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    # USERNAME_FIELD = 'name'
    
    # def __str__(self):
    #     return self.name





