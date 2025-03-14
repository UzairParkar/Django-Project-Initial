from django.contrib import admin
from myapp.models import Userinfo

@admin.register(Userinfo)
class infoadmin(admin.ModelAdmin):
    list_display = ('id','name','age','place','created_at','updated_at')

    
    list_filter = ('id','age')

# Register your models here.

