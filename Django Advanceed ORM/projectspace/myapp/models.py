from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=False,unique=True)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name}'
    
class Posts(models.Model):
    Title = models.CharField(max_length=30,null=True)
    Content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,related_name='posts')

    def __str__(self):
        return f'{self.Title} \t {self.Content} \t {self.created_at} \t {self.updated_at} \t {self.user}'
    


    