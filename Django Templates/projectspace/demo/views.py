from django.shortcuts import render, HttpResponse
import os
from myproject.settings import BASE_DIR
# Create your views here.

def index(request):
    '''When the user comes to 127.0.0.1:8000. 
    urls are checked in the myproject.urls. 
    then they are forwarded to demoap.urls where
    the url checks which enpoint has been called 
    and response is rendered'''
    context = {
        "message":"This is a message stored in a variable and will be displayed when the user is on the home page"
    }
    return render(request,'base.html',context)

def about(request):
    '''same for the about page on 127.0.0.1:8000/about'''
    context = {
        'message':"This is a message stored in a variable and will be displayed when the user is on the about page"
    }
    return render(request,'about.html',context)


def services(request):
    '''Same for the services page on 127.0.0.1:8000/services'''
    context = {
        'message':"This is a message stored in a variable and will be displayed when the user is on the services page"
    }
    return render(request,'services.html',context)


def contact(request):
    context = {
        'message':"This is a message stored in a variable and will be displayed when the user is on the contact page"
    }
    '''A contact Page for the app on 127.0.0.1:8000/contact'''
    return render(request,'contact.html',context)