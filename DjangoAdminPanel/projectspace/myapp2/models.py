from django.db import models
from myapp.models import Person

class Pets(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updtedat = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(Person,on_delete=models.CASCADE,related_name='pets')
    def __str__(self):
        return f'{self.name} \t {self.createdat} \t {self.updtedat}'