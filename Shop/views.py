from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SearchForm, ProductForm, CommentForm
from .utils import render_to_pdf
from Shop.models import Product, Comment

''' Home View '''


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
            products_found = Product.objects.all()
            ids = []
            for product in products_found:
                if (product.get_average() == int(search_string_text)):
                    ids.append(product.id)
            products_found = Product.objects.filter(id__in=ids)
        elif search_string_category == "Instagram Name":
            if '@' in search_string_text:
                products_found = Product.objects.filter(creator__instagram_handle__contains=search_string_text)
            else:
                products_found = Product.objects.filter(creator__instagram_handle__contains='@' + search_string_text)

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'all_the_products': products_found,
                   'show_results': True}
        return render(request, 'Shop/home.html', context)

    else:
        form_in_function_based_view = SearchForm()
        all_the_products = Product.objects.all()
        context = {'form': form_in_function_based_view,
                   'all_the_products': all_the_products,
                   'show_results': True}
        return render(request, 'Shop/home.html', context)


''' Cart View '''


def cart(request):
    context = {}
    return render(request, 'Shop/cart.html', context)


''' Product Add '''


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Shop/upload.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


''' Checkout View '''


def checkout(request):
    context = {}
    return render(request, 'Shop/checkout.html', context)


''' Detail View '''


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
    comments_downvotes = []
    for comment in comments:
        comments_downvotes.append(comment.get_downvotes_count())

    comments_upvotes = []
    for comment in comments:
        comments_upvotes.append(comment.get_upvotes_count())

    comments_flags = []
    for comment in comments:
        comments_flags.append(comment.get_flags_count())

    context = {'that_one_product': that_one_product,
               'comments_for_that_one_product': comments,
               'comments_downvotes': comments_downvotes,
               'comments_upvotes': comments_upvotes,
               'comments_flags': comments_flags,
               'number_of_votes': that_one_product.get_number_of_votes(),
               'avg': that_one_product.get_average(),
               'comment_form': CommentForm}

    can_comment = False
    user = request.user
    if not user.is_anonymous:
        can_comment = True
        # Add if shopUser has its own types
        # shopUser = ShopUser.objects.get(user=user)
        # can_delete = shopUser.candelete()
        context['can_comment'] = can_comment

    return render(request, 'Shop/detail.html', context)


''' PDF View '''


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        that_one_product = Product.objects.get(id=product_id)
        context = {
            'that_one_product': that_one_product,
        }
        pdf = render_to_pdf('Shop/utils/productinfo.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


''' Product Search View '''


# old code? [JNR]

def product_search(request):
    if request.method == 'POST':
        search_string_text = request.POST['title']
        products_found = Product.objects.filter(title__contains="Sonnenuntergang")

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'products_found': products_found,
                   'show_results': True}
        return render(request, 'Shop/home.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'Shop/home.html', context)


''' Vote Product View '''


@login_required(login_url='login')
def vote(request, pk: str, rating: str):
    product = Product.objects.get(id=int(pk))
    user = request.user
    product.vote(user, rating)
    return redirect('detail', pk=pk)


''' Vote Comment View '''


@login_required(login_url='login')
def comment_vote(request, pk: int, cid: int, up_or_down_or_flag: str):
    product = Product.objects.get(id=int(pk))
    comment = Comment.objects.get(id=int(cid))
    user = request.user
    comment.vote(user, up_or_down_or_flag)
    return redirect('detail', pk=pk)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'Shop/edit.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        can_update = False

        if not user.is_anonymous and self.request.user == self.get_object().creator:
            can_update = True
            context['can_update'] = can_update
            return context
