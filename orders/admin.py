from django.contrib import admin

from orders import models


@admin.register(models.Pizza)
class Pizzadmin(admin.ModelAdmin):
    list_display = ('flavor', 'size', 'quantity')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'customer_address')
