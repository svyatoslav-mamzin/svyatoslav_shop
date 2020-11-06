from django.contrib import admin
from .models import Cart_bd, CartItem

class OrderItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']

@admin.register(Cart_bd)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid']
    list_filter = ['paid']
    inlines = [OrderItemInline]


admin.site.register(CartItem)