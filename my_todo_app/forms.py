from django import forms
from .models import StaffBiodata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffBiodata
        fields = '__all__'
        labels = {

        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['phone'].required = False

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

