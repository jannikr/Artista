from django.shortcuts import render

# Create your views here.
def profile(request):
    context = {}
    return render(request, 'Profile/profile.html', context)

def signin(request):
    context = {}
    return render(request, 'Profile/login.html', context)

def signup(request):
    context = {}
    return render(request,'Profile/signup.html', context)