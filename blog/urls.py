from django.urls import path
from blog.views import PostListView, CategoryPageView
from blog import views


post_urlpatterns = ([
    path('', PostListView.as_view(), name='post_list'),
    path('category/<int:category_id>', CategoryPageView.as_view(), name="category"),
], 'posts')