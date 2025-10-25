from django.urls import path
from .views import MenuListCreateView, MenuDetailView

urlpatterns = [
    path('menu/', MenuListCreateView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),
]
