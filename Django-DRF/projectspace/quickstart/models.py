from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100,null=False)
    place = models.CharField(max_length=100,null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} \t {self.place}'