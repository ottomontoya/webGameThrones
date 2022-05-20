from django.urls import path
from core import views
#from core.views import HomePageView

core_urlpatterns = ([
    path('', views.home, name='home'),
    #path('', .as_view(), name='home'),
    path('history/', views.history, name='history'),
    path('characters/', views.characters, name='characters'),

], 'core')
