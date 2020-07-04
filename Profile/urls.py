from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.MySignupView.as_view(), name="signup"),
]