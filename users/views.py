from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import *
from .form import RegisterCustomerForm


def RegisterCustomer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.save()
            messages.info(request, 'Your account has been successfully registered. Please login to continue')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong, Please check form inputs')
            return redirect('register_customer')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request, 'users/register_customer.html', context)


#login a user

def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login successfully. Please enjoy your session')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong, Please check form inputs')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def LogoutUser(request):
    logout(request)
    messages.info(request, 'Your session has ended. Please login in to continue')
    return redirect('login')