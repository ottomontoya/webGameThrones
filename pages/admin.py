from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    ordering = ('title',)
    search_fields = ('title', 'content',)
    list_display = ('title', 'updated')

admin.site.register(Page, PageAdmin)
