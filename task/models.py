from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('waiter', 'Waiter'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = None
    user_permissions = None

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Dish(models.Model):
    name = models.CharField(_("name"), max_length=100)
    description = models.TextField(_("description"), blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_distance_km = models.FloatField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered'),
    ), default='pending')

    def calculate_estimated_time(self):
        """
                Yetkazib berish vaqtini hisoblash: har 5 minutda 4 ta taom + har km uchun 3 minut.
        """
        total_dishes = sum(item.quantity for item in self.items.all())
        preparation_time = (total_dishes // 4) * 5
        delivery_time = self.delivery_distance_km * 3
        return preparation_time + delivery_time

    def total_dishes(self):
        return sum(item.quantity for item in self.items.all())

    def delivery_time(self):
        return self.calculate_estimated_time()

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.dish.name}"
