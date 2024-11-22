from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from task.models import User, Dish, Order, OrderItem


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role')
    list_display_links = ('id', 'username')
    list_filter = ('role',)


@admin.register(Dish)
class DishAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'price', 'is_available')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('is_available',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_dishes', 'delivery_time', 'status', 'created_at')
    list_display_links = ('id', 'user')
    list_filter = ('status', 'created_at')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'dish', 'quantity')
    list_display_links = ('id',)
