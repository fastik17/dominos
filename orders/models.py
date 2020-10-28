from django.db import models

from authentication.models import User
from orders.contastans import PizzaFlavorChoices, PizzaSizeChoices, StatusChoices


class Pizza(models.Model):
    flavor = models.CharField(max_length=255, choices=PizzaFlavorChoices.choices())
    size = models.CharField(max_length=255, choices=PizzaSizeChoices.choices())
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'pizza'
        verbose_name_plural = 'Pizzas'
        verbose_name = 'Pizza'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.flavor}, {self.size}"


class Order(models.Model):
    pizza = models.ManyToManyField(Pizza, related_name='pizza')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    customer_address = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=255, choices=StatusChoices.choices(), default=StatusChoices.ORDER_PLACED.name)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = 'order'
        verbose_name_plural = 'Orders'
        verbose_name = 'order'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.customer}, {self.customer_address}"
