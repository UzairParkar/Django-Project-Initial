from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=100)
    model = models.IntegerField()
    price = models.CharField(max_length=100,null=False)
    software_v = models.CharField(max_length=10,null=False)


    def __str__(self):
        return self.name
    

    