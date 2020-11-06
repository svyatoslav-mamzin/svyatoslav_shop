from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from cart.models import CartItem, Cart_bd
from shop.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """

        if isinstance(request.user, AnonymousUser):
            self.cart = []
            self.cart_item = None
        else:
            cart = Cart_bd.objects.get(user=request.user)
            self.cart = cart
            self.cart_item = CartItem.objects.filter(cart=self.cart)

    def get_items_cart(self):

        return self.cart_item

    def __len__(self):

        # Count all items in the cart.
        if self.cart_item:
            return self.cart_item.count()
        return 0

    def _update_cart(self, product, quantity):
        cart_item = self.cart_item.get(product=product)
        cart_item.quantity += quantity
        cart_item.save(update_fields=["quantity"])

    def add(self, product, quantity=1):
        # Add a product to the cart or update its quantity.
        if self.cart_item.filter(product=product):
            self._update_cart(product, quantity)
        else:
            cart_item = CartItem(cart=self.cart, product=product, price=product.retail_price, quantity=quantity)
            cart_item.save()

    def remove(self, product):
        # Remove a product from the cart.

        self.cart_item.filter(product=product).first().delete()

    def get_total_price(self):
        return self.cart.get_total_cost()

    def clear(self):
        pass
