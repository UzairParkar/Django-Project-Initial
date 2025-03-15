from django.shortcuts import render, HttpResponse
from myapp.models import Users, Posts

# Create your views here.
def home(request):
    return HttpResponse('Welcome to my Website')
