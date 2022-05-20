from django.urls import path
from pages.views import PageView


page_urlpatterns = ([
    path('<int:page_id>', PageView.as_view(), name="page"),
], 'pages')