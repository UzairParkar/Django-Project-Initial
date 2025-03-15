from django.contrib import admin
from myapp.models import Users, Posts
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','age','created_at','updated_at','is_active')

    list_filter = ('id','name')
    
    list_editable = ('is_active',)

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','Title','Content','created_at','updated_at','user')

    list_filter = ('id','user')