from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    '''When the user comes to 127.0.0.1:8000. 
    urls are checked in the myproject.urls. 
    then they are forwarded to demoap.urls where
    the url checks which enpoint has been called 
    and response is rendered'''
    return HttpResponse("This is a home page")

def about(request):
    '''same for the about page on 127.0.0.1:8000/about'''
    return HttpResponse('This is the about page')


def services(request):
    '''Same for the services page on 127.0.0.1:8000/services'''
    return HttpResponse('This is the services page')


def contact(request):
    '''A contact Page for the app on 127.0.0.1:8000/contact'''
    return HttpResponse('This is the contact page')