from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name="signup")
]