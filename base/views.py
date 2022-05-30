from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import UserCreationForm,NameForm
from .models import Contact


# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            
            
            
            return 'Hello Smith'
    else:
        form = UserCreationForm()
    return render(request, 'base/get_name.html',{'form':'form'})    



def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            Form.save()
            form = UserCreationForm()
            return HttpResponseRedirect('/Thanks/')
        
    else:
        form = NameForm()
        
    return render(request,'base/contact.html',{'form':form})    


def home(request):
    return render(request,'base/home.html')




def about(request):
    return render(request,'base/about.html')

def services(request):
    return render(request,'base/services.html')
