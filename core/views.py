from django.shortcuts import render, redirect
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

def add_to_cart(request, id):
    user = request.user
    print("ID: ", id)

    if user.is_authenticated:
        if request.method == "POST":
            product = Product.objects.get(id=id)
            quantity = int(request.POST.get('quantity', 1))
            # Check if user already has a cart
            print("Before order creation")
            order, created = Order.objects.get_or_create(user=user)
            print("After order creation")
            print("Created: ", created)
            # Add product to cart
            cart_item, created = order.items.get_or_create(product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()  # Save cart item outside the conditional
            order.total_price = order.calculate_total_price
            order.save()
            return redirect('products')
        else:
            return render(request, "core/product.html")
    else:
        return render(request, "core/product.html")
    

    print(f"Add to cart for product {id}")
    context = {

    }
    return render(request, "core/cart.html", context)
