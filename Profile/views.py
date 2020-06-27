from django.shortcuts import render

# Create your views here.
def profile(request):
    context = {}
    return render(request, 'Profile/profile.html', context)

def signin(request):
    context = {}
    return render(request, 'Profile/signin.html', context)

def signup(request):
    context = {}
    return render(request,'Profile/signup.html', context)