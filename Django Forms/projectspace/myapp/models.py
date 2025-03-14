from django.db import models

# Create your models here.
class Userinfo(models.Model):
    name = models.CharField(max_length=200,null=False)
    age = models.IntegerField(null=True)
    place = models.CharField(max_length=50)
    about = models.TextField(max_length=1200)
    services = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True) # <- used when object is first created
    updated_at = models.DateTimeField(auto_now=True) # used when object is saved

    def __str__(self):
        return f'{self.name} | {self.age} | {self.place}'
    
    