from django.db import models

# Create your models here.
#---
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    #we can make the fdefault username field none and make the email the username for now.

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    


