from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your_name', max_length=100)
class UserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model  = User
        fields ='__all__'

