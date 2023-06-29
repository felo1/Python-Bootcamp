from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.models import Group, User
# Create your views here.

def index(request):
    return render(request, 'app/index.html')
