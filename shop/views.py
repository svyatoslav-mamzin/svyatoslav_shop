from django.shortcuts import render, get_object_or_404

from svyatoslav_shop.shop.models import Product
from svyatoslav_shop.shop.services.db_model_service import get_available_products


def product_list(request):
    products = get_available_products()
    data = {'products': products}
    return render(request, 'shop/product/list.html', context=data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


