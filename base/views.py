from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def contact(request):
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse('<h1>Thanks for contacting us</h1>')
    return render(request,'base/contact.html')

def about(request):
    return render(request,'base/about.html')

def services(request):
    return render(request,'base/services.html')
