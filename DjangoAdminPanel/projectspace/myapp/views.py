from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('HEllo World')

def about(request):
    pass

def services(request):
    pass

def contact(request):
    pass