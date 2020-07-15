from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('upload/', views.ProductCreateView.as_view(), name="upload"),
    path('add/<int:pk>/', views.addtocart, name='addtocart'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/pdf/', views.GeneratePdf.as_view(), name='pdf'),
    path('detail/<int:pk>/vote/<str:rating>/', views.vote, name='product-vote'),
    path('detail/<int:pk>/comment/<int:cid>/vote-comment/<str:up_or_down_or_flag>/', views.comment_vote, name='comment-vote'),
]
