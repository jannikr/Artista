from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from Shop.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'all_the_products'
    template_name = 'Shop/home.html'

def cart(request):
    context = {}
    return render(request, 'Shop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Shop/checkout.html', context)

def detail(request):
    context = {}
    return render(request, 'Shop/detail.html', context)