from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    username = models.CharField(max_length=29,null=False,unique=True)
    email = models.EmailField(max_length=27,unique=True)
    age = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_moderator = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        swappable = "AUTH_USER_MODEL"

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Forum(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
from django.db import models
from .models import CustomUser, Forum

class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.forum.title}"


class Star(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')  # Ensure only one star per user per comment.

    def __str__(self):
        return f"Star by {self.user.username} on comment {self.comment.id}"