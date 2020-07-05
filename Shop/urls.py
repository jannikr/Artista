from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('detail/', views.detail, name="detail")
]