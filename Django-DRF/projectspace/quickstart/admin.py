from django.contrib import admin
from quickstart.models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','place','created_at','updated_at','is_active']
    list_editable = ['is_active']