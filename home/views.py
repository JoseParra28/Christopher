from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import ItemCategory, ItemProduct



def index(request):
    return render(request, 'home/index.html')


def all_products(request):
    products = ItemProduct.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category_name_in=categories)
            categories = ItemCategory.objects.filter(name_in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter a valid search criteria")
                return redirect(reverse('products'))

            queries = Q(name_icontains=query) | Q(description_icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term':query,
        'current_categories': categories
    }
    return render(request,'home/products.html' , context)    
