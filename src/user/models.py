from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.contrib.auth.models import AbstractUser
# # Create your models here.
class User(AbstractUser):
    """
    User model to store user data
    """
