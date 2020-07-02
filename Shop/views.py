from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'Shop/home.html', context)

def cart(request):
    context = {}
    return render(request, 'Shop/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'Shop/checkout.html', context)

def detail(request):
    context = {}
    return render(request, 'Shop/detail.html', context)