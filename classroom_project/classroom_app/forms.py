from django import forms
from django.contrib.auth.models import User
from .models import Classroom

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ClassroomCreationForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']

class JoinClassroomForm(forms.Form):
    code = forms.UUIDField()
