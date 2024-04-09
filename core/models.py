from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid


# User = get_user_model()
User = settings.AUTH_USER_MODEL

print("USer: ", User)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', default="images/download (3).jpeg/")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def calculate_total_price(self):
        total_price = sum(item.subtotal for item in self.items.all())
        print("All order items: ", self.items.all())
        return total_price

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", null=True)
    quantity = models.PositiveIntegerField(null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    @property
    def subtotal(self):
        return self.product.price * self.quantity
