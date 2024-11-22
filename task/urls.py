from django.urls import path
from .views import DishListCreateView, DishRetrieveUpdateDestroyView, OrderListView, OrderCreateView

urlpatterns = [
    path('dishes/', DishListCreateView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishRetrieveUpdateDestroyView.as_view(), name='dish-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
]
