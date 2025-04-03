from django.shortcuts import render, HttpResponse
from myapp.models import User
# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def create(request):
    user = [User(name=f'tester{i}',age=f'{i}',place = f'Mumbai')for i in range(2,30)]
    User.objects.bulk_create(user)
    return HttpResponse('Creation Sucessful')

def delete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return HttpResponse("Deletion sucessfully")