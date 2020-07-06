from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import ShopUserCreationForm

# Create your views here.
class MySignupView(generic.CreateView):
    form_class = ShopUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def user(request):
    context = {}
    return render(request, 'profile.html', context)