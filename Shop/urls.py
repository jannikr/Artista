from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('upload/', views.ProductCreateView.as_view(), name="upload"),
    # path('detail/', views.detail, name="detail"),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/vote/<str:rating>/', views.vote, name='product-vote')
]
