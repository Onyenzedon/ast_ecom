from django.shortcuts import render
from .models import Product, ProductImage, Order, OrderItem, Category

# Create your views here.

def index(request):
    products = Product.objects.all()[:6]
    context = {
        'products' : products
    }
    return render(request, 'core/index.html', context)

def landing(request):
    return render(request, 'core/landing.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'core/products.html', context)

def product(request, id):
    product = Product.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request, 'core/product.html', context)

def add_to_cart(request,id):

    print(f"Add to cart for product {id}")
    context = {

    }
    return render(request, "core/cart.html", context)
