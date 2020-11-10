from django.http import HttpResponse
from django.shortcuts import render

from account.models import Profile
from cart.cart import Cart
from .models import Order, OrderItem
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(client=request.user,
                                 delivery_address=Profile.objects.get(user=request.user).delivery_address)
    list_items = []
    for item in cart.get_items_cart():
        list_items.append(OrderItem(order=cart, product=item.product,
                                    price=item.price, quantity=item.quantity))
    OrderItem.objects.bulk_create(list_items)

    order_created.delay()
    return render(request,
                  'orders/order.html',
                  {'order': order, 'items': cart.get_items_cart()})
