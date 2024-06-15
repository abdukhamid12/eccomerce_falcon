from django.shortcuts import render, get_object_or_404

from eccomerce.models import *


# Create your views here.
def store(request):
    # return render(request, 'store/e-commerce/product/product-list.html', context)
    # return render(request, 'store/e-commerce/product/product-details.html', context)
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/e-commerce/product/product-grid.html', context)
    # return render(request, 'base.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/e-commerce/product/product-list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }
    return render(request, 'store/e-commerce/product/product-details.html', context)


def order_list(request):
    context = {}
    return render(request, 'store/e-commerce/orders/order-list.html', context)


def order_details(request):
    context = {}
    return render(request, 'store/e-commerce/orders/order-details.html', context)


def customers(request):
    context = {}
    return render(request, 'store/e-commerce/customers.html', context)


def customers_details(request):
    context = {}
    return render(request, 'store/e-commerce/customer-details.html', context)


def shopping_cart(request):
    context = {}
    return render(request, 'store/e-commerce/shopping-cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/e-commerce/checkout.html', context)


def billing(request):
    context = {}
    return render(request, 'store/e-commerce/billing.html', context)


def invoice(request):
    context = {}
    return render(request, 'store/e-commerce/invoice.html', context)
