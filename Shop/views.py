from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .forms import SearchForm
from Shop.models import Product


def home(request):
    if request.method == 'POST':
        search_string_text = request.POST['title']
        search_string_category = request.POST['myCategory']

        if search_string_category == "Titel":
            products_found = Product.objects.filter(title__contains=search_string_text)
        elif search_string_category == "Beschreibung":
            products_found = Product.objects.filter(description__contains=search_string_text)
        elif search_string_category == "Bewertung":
            # To Do
            products_found = Product.objects.filter(title__contains=search_string_text)
            print("-------------------------------------------------")
            print("IMPORTANT:")
            print("Rate function not implemented yet: Shop/views.py")
            print("-------------------------------------------------")
        elif search_string_category == "Instagram Name":
            if '@' in search_string_text:
                products_found = Product.objects.filter(creator__instagram_handle__contains=search_string_text)
            else:
                products_found = Product.objects.filter(creator__instagram_handle__contains='@' + search_string_text)


        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'all_the_products': products_found,
                   'show_results': True}
        return render(request,'Shop/home.html', context)

    else:
        form_in_function_based_view = SearchForm()
        all_the_products = Product.objects.all()
        context = {'form': form_in_function_based_view,
                   'all_the_products': all_the_products,
                   'show_results': True}
        return render(request, 'Shop/home.html', context)


def cart(request):
    context = {}
    return render(request, 'Shop/cart.html', context)

def upload(request):
    context = {}
    return render(request, 'Shop/upload.html', context)

def checkout(request):
    context = {}
    return render(request, 'Shop/checkout.html', context)

def detail(request, **kwargs):
    product_id = kwargs['pk']
    that_one_product = Product.objects.get(id=product_id)
    context = {'that_one_product': that_one_product}
    return render(request, 'Shop/detail.html', context)

def product_search(request):
    if request.method == 'POST':
        search_string_text = request.POST['title']
        products_found = Product.objects.filter(title__contains="Sonnenuntergang")

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'products_found': products_found,
                   'show_results': True}
        return render(request,'Shop/home.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'Shop/home.html', context)

