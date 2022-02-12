from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'password' : forms.PasswordInput(),


        }