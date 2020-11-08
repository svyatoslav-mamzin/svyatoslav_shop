from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product
from shop.services.db_model_service import get_available_products
from loguru import logger

logger.add("logs/shop_logs/log.log", format="{time} {level} {message}", level="ERROR",
           rotation="10 MB", compression='zip')



@logger.catch
def product_list(request):
    products = get_available_products()
    username = request.user.username
    cart = Cart(request)
    data = {'username': username, 'cart': cart, 'total_items': cart.__len__()}
    if products:
        data['products'] = products
    return render(request, 'shop/product/list.html', context=data)

@logger.catch
def product_detail(request, id, slug):
    logger.info("test")
    username = request.user.username
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    data = {'product': product, 'cart_product_form': cart_product_form, 'cart': cart, 'username': username,
            'total_items': cart.__len__()}
    return render(request, 'shop/product/detail.html', context=data)
