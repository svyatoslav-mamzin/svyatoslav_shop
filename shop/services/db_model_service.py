from shop.models import Product


def get_available_products():
    return Product.objects.filter(available=True)