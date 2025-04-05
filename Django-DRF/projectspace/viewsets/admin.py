from django.contrib import admin
from viewsets.models import Mobile

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['name','price','model','software_v']

    
# Register your models here.

