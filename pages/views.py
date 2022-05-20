from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Page

class PageView(TemplateView):
    template_name = 'pages/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_id = self.kwargs['page_id']
        page = Page.objects.get(id=page_id)
        context['page'] = page
        return context
