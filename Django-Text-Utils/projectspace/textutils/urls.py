# file created manaually by u/Uzair


from django.urls import path 
from textutils import views

urlpatterns = [
    path('',views.index,name='index'),
    path('task',views.task, name='task'),
    path('analyze',views.analyze,name='analyze'),

]