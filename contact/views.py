from ast import For
from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.conf import settings
#import requests
from django.http import JsonResponse
import time

def ejecutaAJAX(request):
  if request.method == 'POST':
    #Validamos los campos
    opcion = request.POST.get('valor','')
    respuesta = {}
    opciones = {}
    if opcion == '1':
      respuesta['estado'] = 'correcto'
      opciones['1'] = 'Altabrisa'
      opciones['2'] = 'Cholul'
      opciones['3'] = 'La Isla'
      opciones['4'] = 'City center'
      opciones['5'] = 'Galerias'
    elif opcion == '2':
      respuesta['estado'] = 'correcto'
      opciones['1'] = 'Americas'
      opciones['2'] = 'Mayab'
      opciones['3'] = 'Altozano'
    else:
       respuesta['estado'] = 'No valido'
    respuesta['opciones'] = opciones
    time.sleep(0)
    return JsonResponse(respuesta) 

class ContactFormView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        pos_arroba = email.find("@")
        dominio = email[pos_arroba+1:]
        #Se valida que el dominio del correo sea gmail.com
        #if dominio != 'gmail.com':
        #    form.add_error('email','Dominio inválido')
        #    form.add_error('email','Debes tener cuenta de gmail')
        #    return self.form_invalid(form)
        #Se envía un correo 
        content = form.cleaned_data.get("content")
        subject = "Gracias por tus comentarios"
        message = f"{name}, gracias por contactarnos."
        message += "\n\n********************************** \n\n" + content
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        #response = requests.get('http://localhost:3000/tareas','')
        #print(response.json())
        send_mail(subject, message, email_from, recipient_list)
        return super().form_valid(form)
