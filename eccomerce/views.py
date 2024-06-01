from django.shortcuts import render



# Create your views here.
def store(request):
    context = {}
    return render(request, 'store/e-commerce/product/product-list.html', context)