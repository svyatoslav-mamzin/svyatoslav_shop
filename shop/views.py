from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Product
from shop.services.db_model_service import get_available_products


#@login_required
def product_list(request):
    products = get_available_products()
    username = request.user.username
    data = {'products': products, 'username': username}
    return render(request, 'shop/product/list.html', context=data)


#@login_required
def product_detail(request, id, slug):
    username = request.user.username
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    data = {'product': product, 'cart_product_form': cart_product_form, 'username': username}
    return render(request, 'shop/product/detail.html', context=data)
