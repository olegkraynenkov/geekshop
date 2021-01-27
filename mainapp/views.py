from django.shortcuts import render
from datetime import datetime
from mainapp.models import Product, ProductCategory

# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop store'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    now = str(datetime.now())[:4]
    context = {
        'year': now,
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
