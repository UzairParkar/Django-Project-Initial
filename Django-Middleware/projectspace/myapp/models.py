from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,null=False)
    age = models.IntegerField(null=True)
    place = models.CharField(max_length=120,null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name