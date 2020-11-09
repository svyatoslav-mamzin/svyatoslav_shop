from django.contrib import admin
from .models import Cart_bd, CartItem


class OrderItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']


#@admin.register(Cart_bd)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'paid']
    list_filter = ['paid']
    inlines = [OrderItemInline]

    def queryset(self, request):
        if request.user.is_superuser:
            return super(CartAdmin, self).queryset(request)
        else:
            qs = super(CartAdmin, self).queryset(request)
            return qs.filter(user=request.user)

admin.site.register(Cart_bd,CartAdmin)
