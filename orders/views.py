from django.http import HttpResponse
from account.models import Profile
from cart.cart import Cart
from .html_creater import html_creater
from .models import Order, OrderItem
from .tasks import order_created
from loguru import logger

logger.add("logs/orders/log", format="{time} {level} {message}", level="ERROR",
           rotation="10 MB", compression='zip')

@logger.catch
def order_create(request):
    cart = Cart(request)
    profile = Profile.objects.get(user=request.user)

    order = Order.objects.create(client=request.user,
                                 delivery_address=profile.delivery_address)
    list_items = []
    for item in cart.get_items_cart():
        list_items.append(OrderItem(order=order, product=item.product,
                                    price=item.price, quantity=item.quantity))
    OrderItem.objects.bulk_create(list_items)
    logger.info(f"заказ №{order.id} создан")
    html_text = html_creater(request.user.username, order, cart)
    order_created.delay(html_text, order.id)
    cart.clear()
    return HttpResponse(html_text)
