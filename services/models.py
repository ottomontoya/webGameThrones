from distutils.command.upload import upload
from email.mime import image
from importlib.resources import contents
from pyexpat import model
from sqlite3 import Date
from tabnanny import verbose
from tokenize import Number
from turtle import title, update
from django.db import models


class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    correo = models.EmailField(verbose_name="Email")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.CharField(max_length=200, verbose_name="Calle y Numero")
    colonia = models.CharField(max_length=200, verbose_name="Colonia")
    total = models.DecimalField(verbose_name="Total", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha']

    def __str__(self):
        return str(self.id)


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nombre del servicio')
    title2 = models.CharField(max_length=100, verbose_name='Empresa que ofrecio el servicio')
    Date = models.DateField(verbose_name='Fecha de termino del servicio')
    description = models.TextField(verbose_name='Descripcion del servicio')
    image = models.ImageField(verbose_name='Imagen', upload_to="services")
    Number = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Costo del servicio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
        #   Orden por default
        ordering = ['-Date']
