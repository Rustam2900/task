from rest_framework import generics, permissions
from .models import Dish, Order
from .serializers import DishSerializer, OrderSerializer, OrderCreateSerializer


class IsAdminOrWaiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'waiter']


class DishListCreateView(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), IsAdminOrWaiter()]
        return [permissions.AllowAny()]


class DishRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrWaiter]


# Order Views
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'user':
            return self.queryset.filter(user=self.request.user)
        return self.queryset


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
