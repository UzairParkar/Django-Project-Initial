from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=30,null=False,unique=True)
    age = models.IntegerField(null=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updtedat = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} \t {self.createdat} \t {self.updtedat}'