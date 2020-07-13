from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from Shop.models import Product
from .forms import ShopUserCreationForm

# Create your views here.
class MySignupView(generic.CreateView):
    form_class = ShopUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserListView(ListView):
    # maybe change to function based view and filter products only from self.user
    # products = Product.objects.filter(product=all_the_products__contains__creator_id...)
    model = Product
    context_object_name = 'all_the_products'
    template_name = 'profile.html'