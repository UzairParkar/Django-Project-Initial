from django.contrib import admin
from myapp.models import Person
from myapp2.models import Pets



admin.site.site_header = "Admin Interface"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to My Custom Admin Interface"

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','age','createdat','updtedat','is_active')

    list_filter = ('id','name','createdat')

    search_fields = ('is_active','id')

    date_hierarchy = 'createdat'

    
@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id','owner','name','createdat','updtedat','age','is_active')

    list_filter = ('id','name','createdat')

    search_fields = ('is_active','id')

    list_editable = ('is_active',)

    



# Register your models here.
