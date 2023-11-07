
from django.urls import path
from . import views

urlpatterns = [
    path('register_customer', views.RegisterCustomer, name='register_customer'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout')
]

