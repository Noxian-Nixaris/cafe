from django.contrib import admin

from orders.models import Dish, Order


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    model = Dish
    list_display = ('name', 'price')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('table_number', 'total_price', 'status')
    filter_horizontal = ('items',)
