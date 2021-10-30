from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="students-home"),
    path('profile/', views.profile, name="students-profile"),
    path('wishlist/', views.wishlist, name="students-wishlist"),
    path('applied/', views.applied, name="students-applied"),
]