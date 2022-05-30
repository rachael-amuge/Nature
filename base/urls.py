from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('get_name/',views.get_name, name='get_name'),
]