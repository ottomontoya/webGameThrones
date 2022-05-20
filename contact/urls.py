from unicodedata import name
from django.urls import path 
from contact.views import ContactFormView
from django.views.generic import TemplateView
from .views import ejecutaAJAX

contact_urlpatterns = ([
    path('', ContactFormView.as_view(), name='contact'),
    path('thanks/', TemplateView.as_view(template_name='contact/thanks.html'), name='thanks'),
    path('ejecutaAJAX/', ejecutaAJAX, name='ejecutaAJAX'),
], 'contact')