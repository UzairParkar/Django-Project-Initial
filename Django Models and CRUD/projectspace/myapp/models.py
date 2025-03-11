from django.db import models
from datetime import datetime

# Create your models here.

class Person(models.Model):
    username = models.CharField(max_length=30,null=True,unique=True)
    email = models.CharField(max_length=15,null=False,unique=True)
    age = models.IntegerField(null=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updtedat = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__ (self):
        return f'{self.username}\t{self.email}'
    
