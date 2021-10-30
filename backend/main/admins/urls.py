from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admins-home'),
    path('newupevent/', views.newupevent, name='admins-newupevent'),
]