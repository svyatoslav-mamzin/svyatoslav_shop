from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'available', 'purchase_price', 'retail_price']
    list_filter = ['available']



