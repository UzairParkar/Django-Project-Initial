from django.urls import path
from forums import views
urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register, name='register'),
    path('login',views.login_view, name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout_view,name='logout')
    ]