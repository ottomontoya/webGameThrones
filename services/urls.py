from .import views
from django.urls import path
from .views import PedidoSuccess, ServiceCreatePedido, ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView

service_urlpatterns = ([
    path('', ServiceListView.as_view(), name='services_list'),
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('update/<int:pk>', ServiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ServiceDeleteView.as_view(), name='delete'),
    path('pedido/', views.realizar_pedido, name='detalle_pedido'),
    path('create_pedido/', ServiceCreatePedido.as_view(), name='create_pedido'),
    path('success_pedido/', PedidoSuccess.as_view(), name='success_pedido'),
], 'services')