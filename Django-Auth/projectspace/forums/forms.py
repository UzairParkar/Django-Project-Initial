from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import PasswordChangeForm
from django import forms

CustomUser = get_user_model()

class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='password'
    )

    class Meta:
        model = CustomUser
        fields = ['username','age','email','password1','password2']
