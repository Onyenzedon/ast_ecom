from django.contrib import admin
from .models import Product, ProductImage, Order, OrderItem, Category
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_id', 'total_price', 'created_at']
    readonly_fields = ['order_id', 'total_price', 'created_at']

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Category)