from django.shortcuts import render, redirect
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .models import *
#from .forms import OrderForm, CreateUserForm
from django.contrib.auth import authenticate, login,logout
#from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
#from .decorators import unauthenticated_user, allowed_users,admin_only




from .models import *


# Create your views here.

#HOME PAGE VIEW

def home(request):
    return render(request, 'users/home.html')

# About View Function

def about(request):
    return render(request, 'users/about.html')

# Contact View Funcction

def contact(request):
    return render(request, 'users/contact.html')