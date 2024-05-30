from django.shortcuts import render

from eccomerce.models import Product


# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/e-commerce/product/product-details.html', context)