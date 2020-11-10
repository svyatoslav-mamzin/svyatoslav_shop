from django.contrib.auth.models import User
from django.db import models
from shop.models import Product
from decimal import Decimal


class Cart_bd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Cart {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost


class CartItem(models.Model):
    cart = models.ForeignKey(Cart_bd,
                             related_name='items',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='cart_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
