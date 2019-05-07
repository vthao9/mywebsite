from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.models import User

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Need to be all uppercase")

    return value

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
