from django.shortcuts import render
from .models import ItemCategory, ItemProduct


def index(request):
    return render(request, 'home/index.html')


def all_products(request):
    products = ItemProduct.objects.all()
    ctx = {
        'products': products
    }
    return render(request,'home/products.html' , ctx)    
