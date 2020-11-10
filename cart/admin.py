from django.contrib import admin
from .models import Cart_bd, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']


@admin.register(Cart_bd)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    inlines = [CartItemInline]

    def queryset(self, request):
        if request.user.is_superuser:
            return super(CartAdmin, self).queryset(request)
        else:
            qs = super(CartAdmin, self).queryset(request)
            return qs.filter(user=request.user)

