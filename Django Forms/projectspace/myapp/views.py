from django.shortcuts import render, HttpResponse, redirect
from myapp.forms import UserinfoForm
from myapp.models import Userinfo

# Create your views here.
def home(request):
    alllist = Userinfo.objects.all()
    if request.method == 'POST':
        form = UserinfoForm(request.POST)
        if form.is_valid(): # <- checks if form has no errors or not
            form.save()
            redirect('home')
    else:
        form = UserinfoForm()

    return render(request,'index.html',{'form':form,'alllist':alllist})


