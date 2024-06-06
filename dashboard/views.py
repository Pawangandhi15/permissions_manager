from django.shortcuts import render
from .models import Product, Order, Customer

def dashboard_view(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {
        'products': products,
        'orders': orders,
        'customers': customers,
    }
    return render(request, '/dashboard/dashboard.html', context)
