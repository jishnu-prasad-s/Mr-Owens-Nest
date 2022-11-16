from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    :model: `accounts.User`
    Custom User Model
    
    """
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    
    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        # swappable = 'AUTH_USER_MODEL'