from django.shortcuts import render, HttpResponse, redirect
from forums.forms import CustomUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'base.html')

def register(request):

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user_group, created = Group.objects.get_or_create(name="authenticated_user")
            user.groups.add(user_group)
            form = CustomUserForm()
            user.save()
            return redirect('index')
    else:
        form = CustomUserForm()
    return render(request, 'home.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.logged_in = True
            user.save()
            login(request, user)

            return redirect('dashboard')
    return render(request, 'login.html')
     


@login_required
def dashboard(request):
    user = request.user
    user_attributes = {
        "Username": user.username,
        "Email": user.email,
        "age":user.age,
        "Date Joined": user.date_joined,
    }
    return render(request,'dashboard.html',{'user_attributes':user_attributes})


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        request.user.logged_in = False
        request.user.save()
    logout(request)
    return redirect('index')
