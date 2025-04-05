from django.contrib import admin
from mytodo.models import CustomUser, Todo

@admin.register(CustomUser)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username','is_staff','is_active','about','roles']


@admin.register(Todo)
class ToDoAdminModel(admin.ModelAdmin):
    list_display = ['title','date_created','updated_at',"is_completed",'is_public','is_flagged','owner']
