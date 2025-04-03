from django.urls import path
from quickstart import views



urlpatterns = [
    path('',views.getdata,name='getdata'),
    path('read/<int:pk>',views.getby_id,name='getbyid'),
    path('read/<str:place>',views.get_by_place,name='getbyplace'),
    path('add/',views.add_item,name='add_item'),
    path('update/<int:pk>',views.update_item,name='update_item'),
    path('delete/<int:pk>',views.delete_item,name='delete_item')

]