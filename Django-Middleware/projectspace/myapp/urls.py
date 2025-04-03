from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'), 
    path('delete/<int:pk>',views.delete,name='delete')
]