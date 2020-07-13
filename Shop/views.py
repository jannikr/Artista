from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SearchForm, ProductForm, CommentForm
from Shop.models import Product, Comment


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

class ProductCreateView(CreateView):
    print('Hello')
    model = Product
    form_class = ProductForm
    template_name = 'Shop/upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

def checkout(request):
    context = {}
    return render(request, 'Shop/checkout.html', context)

def detail(request, **kwargs):
    product_id = kwargs['pk']
    that_one_product = Product.objects.get(id=product_id)

    # add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.product = that_one_product
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    comments = Comment.objects.filter(product=that_one_product)
    context = {'that_one_product': that_one_product,
               'comments_for_that_one_product': comments,
               'comment_form': CommentForm}
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

