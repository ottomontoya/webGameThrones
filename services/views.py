from dataclasses import fields
from pyexpat import model
from tokenize import Number
from turtle import title
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Services
from django.urls import reverse_lazy
from .forms import PedidoForm
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings


class PedidoSuccess(TemplateView):
    template_name = 'services/pedido_success.html'


class ServiceCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = 'services/pedido_cliente.html'
    success_url = reverse_lazy('services:success_pedido')

    def form_valid(self, form):
        pedido_nuevo = form.save(commit=False)
        pedido_nuevo.save()
        body = crear_cuerpo(self.request.session['detalle_pedido'])
        send_message(pedido_nuevo.correo, 'Pedido confirmado', "Total del pedido {total}".format(total=pedido_nuevo.total)+"\n"+body)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ServiceCreatePedido, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def crear_cuerpo(lista):
    return "".join(str(e) for e in lista)


def _crea_diccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1] #se elimina el ultimo
    productos = datos_pedido.split("|")
    for producto in productos:
        detalle = producto.split("-")
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario


def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        productos = _crea_diccionario(datos_pedido)
        total = 0
        for codigo_barras in productos.keys():
            print(codigo_barras)
            cantidad = productos[codigo_barras]
            if cantidad > 0:
                dict_producto = {}
                servicio = Services.objects.get(pk=codigo_barras)
                print(servicio.id)
                dict_producto['id'] = servicio.id
                dict_producto['descripcion'] = servicio.title
                dict_producto['cantidad'] = cantidad
                #codigo duro
                dict_producto['precio'] = str(servicio.Number)
                total += cantidad * servicio.Number
                pedido.append(dict_producto)
        #se colocan las variables en sesion
        request.session['total_float'] = float(total)
        request.session['detalle_pedido'] = pedido
    return render(request, 'services/detalle_pedido.html',
        {'pedido':pedido, 'total':total})

def send_message(email, subject, content):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, content, email_from, recipient_list)

class ServiceListView(ListView):
    model = Services

class ServiceCreateView(CreateView):
    model = Services
    fields = ['title', 'title2', 'description', 'image']
    success_url = reverse_lazy('services:services_list')

class ServiceUpdateView(UpdateView):
    model = Services
    fields = ['title', 'title2', 'description', 'image']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('services:update',
                args=[self.object.id]) + '?ok'

class ServiceDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy('services:services_list')