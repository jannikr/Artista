from django.urls import path
from . import views

urlpatterns = [
    path('comments-with-flag/', views.CommentsFlagView.as_view(), name='comments-flag'),
]