from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup")
]