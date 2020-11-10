from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Order(models.Model):
    client = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.item.all())
        return total_cost


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='item',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
