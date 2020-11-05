from django.contrib import admin

from shop.models import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'purchase_price', 'retail_price']
    list_filter = ['available', 'purchase_price', 'retail_price']
    list_editable = ['available', 'purchase_price', 'retail_price']
    prepopulated_fields = {'slug':('name',)}
