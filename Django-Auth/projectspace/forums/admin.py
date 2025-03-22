from django.contrib import admin
from forums.models import CustomUser, Forum,Profile,Comment, Star

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
     list_display = ['username','date_joined','date_updated','logged_in','is_staff',]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
     list_display = ['user','bio']


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
     list_display = ['title','author','description','created_at','updated_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
     list_display = ['forum','author','message','created_at','updated_at']

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
     list_display = ['comment','user','created_at']