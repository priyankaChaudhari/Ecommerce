from django.db import models

# Create your models here.
class User(models.Model):
    """
    User model to store user data
    """

    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 80)
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('supplier', 'Supplier'),
    )
    PERMISSION_CHOICES = (
        ('create', 'Create'),
        ('read', 'Read'),
        ('update', 'Update'),
        ('delete', 'Delete')
    )
