from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200,null=False)
    is_perishable = models.BooleanField()
    quantity = models.IntegerField(null=False)
    price = models.CharField(max_length=12)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_displayed = models.BooleanField(default=False)


    def __str__(self):
        return self.name



