from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    search_fields = ('title', 'content', 'author__first_name')
    date_hierarchy = 'published'
    list_filter = ('author__first_name', 'categories__name')

    def post_categories(self, obj):
        res = ""
        for c in obj.categories.all().order_by("name"):
            res += c.name + ", "
        res = res[0:len(res)-2]
        return res
    post_categories.short_description = "Categorías"

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)