from django.contrib import admin
from .models import Category, Product, Order, Payment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer_price', 'categories')
    search_fields = ('name', 'description')
    list_filter = ('categories',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total')
    search_fields = ('user__username',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amount', 'timestamp')
    search_fields = ('user__username',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment,PaymentAdmin)