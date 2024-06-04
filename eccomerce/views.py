from django.shortcuts import render



# Create your views here.
def store(request):
    context = {}
    # return render(request, 'store/e-commerce/product/product-list.html', context)
    # return render(request, 'store/e-commerce/product/product-details.html', context)
    return render(request, 'store/e-commerce/product/product-grid.html', context)
    # return render(request, 'base.html', context)

def product_list(request):
    context = {}
    return render(request, 'store/e-commerce/product/product-list.html', context)

def product_details(request):
    context = {}
    return render(request, 'store/e-commerce/product/product-details.html', context)