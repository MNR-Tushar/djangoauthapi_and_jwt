from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser,PermissionsMixin):

   
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #date_joined = models.DateTimeField(default=timezone.now)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email