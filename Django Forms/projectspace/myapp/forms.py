from django import forms

from myapp.models import Userinfo

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['name','age','place','about','services']