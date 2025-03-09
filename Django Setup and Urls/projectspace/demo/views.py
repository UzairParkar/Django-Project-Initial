from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    '''When you go to 127.0.0.1:8000, the bank path went to the
    url of the project and then it is redirected to home.urls
    the pattern given for this view is views.index'''
    return HttpResponse('This is home page')


def about(request):
    '''When you go to 127.0.0.1:8000'''
    return HttpResponse("This is the about page")

def services(request):
    ''''''
    return HttpResponse('This is a services Page')

def contact(request):
    ''''''
    return HttpResponse('This is the contact Page')
