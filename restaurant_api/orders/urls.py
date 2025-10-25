from django.urls import path
from .views import OrderListCreateView, OrderDetailView, UpdateOrderStatusView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/status/', UpdateOrderStatusView.as_view(), name='order-status'),
]
