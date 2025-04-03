from django.contrib import admin
from classes.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['name','is_perishable','quantity','price','created_at','updated_at','is_displayed']

    list_editable = ['quantity','price','is_perishable','is_displayed']
# Register your models here.
