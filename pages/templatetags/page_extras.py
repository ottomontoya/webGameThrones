from django import template 
from pages.models import Page

#se registra en las librerias
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages