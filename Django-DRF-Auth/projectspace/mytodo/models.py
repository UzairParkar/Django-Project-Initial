from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    about = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    roles = models.CharField(max_length=100,choices=(
        ('Staff','staff'),
        ('Moderator','moderator'),
        ('User','user')
    ),default='User')

    def __str__(self):
        return self.username


class Todo(models.Model):
    title = models.CharField(max_length=50,null=False)
    content = models.CharField(max_length=100,null=False)
    date_created = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser,related_name='todos',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
