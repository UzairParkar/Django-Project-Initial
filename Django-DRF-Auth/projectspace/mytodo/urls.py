from django.urls import path
from mytodo.views import (
    RegisterView, LoginView, LogoutView,
    ListCreateTodoView, RetrieveUpdateDestroyTodoView,
    PublicTodoListView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('todos/', ListCreateTodoView.as_view()),
    path('todos/<int:pk>/', RetrieveUpdateDestroyTodoView.as_view()),
    path('todos/public/', PublicTodoListView.as_view()),
]
