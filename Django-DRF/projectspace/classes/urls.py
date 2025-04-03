from django.urls import path
from classes import views

urlpatterns = [
    path('classes/',views.ProductList.as_view()),
    path('classes/<int:pk>/',views.ProductDetail.as_view())
]