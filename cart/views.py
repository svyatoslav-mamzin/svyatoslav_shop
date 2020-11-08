from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from .models import CartItem, Cart_bd
from loguru import logger

logger.add("logs/cart_logs/{time}_log.log", format="{time} {level} {message}", level="ERROR",
           rotation="10 MB", compression='zip')


@logger.catch
@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'])
    return redirect('cart:cart_detail')


@logger.catch
@login_required
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@logger.catch
@login_required
def cart_detail(request):
    user = request.user
    cart = Cart(request)

    return render(request, 'cart/detail.html', {'username': user.username, 'cart': cart,
                                                'total_items': cart.__len__()})
