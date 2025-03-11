from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from datetime import datetime
from myapp.models import Person

# Create your views here.


def home(request):
    persons = Person.objects.all()
    return render(request,'index.html',{'persons':persons})



def create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        person = Person.objects.create(username=username,email=email,age=age)
        return redirect('home')
    persons = Person.objects.all()
    return render(request,'index.html',{'persons':persons})

def readone(request,pk):
    person = Person.objects.get(id = pk)
    return render(request,'details.html',{'person':person})

def update(request,pk):
    person = Person.objects.get(id=pk)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')

        person.username = username
        person.email = email
        person.age = age
        person.save()
        return redirect('home')
    return render(request, 'update.html', {'person': person})

def delete(request,pk):
    person = Person.objects.get(id = pk)
    if request.method == 'POST':
        person.delete()
        return redirect('home')
    persons = Person.objects.all()
    return render(request,'index.html',{'persons':persons})


