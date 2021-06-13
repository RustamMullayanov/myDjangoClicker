from django.http import JsonResponse
from django.shortcuts import render, redirect
from .my_forms import RegForm
from django.contrib import auth
from django.contrib.auth.models import User
from . import models
import json


def home(request):
    return render(request, 'clicker/home.html')


def clicker(request):
    if request.user.is_authenticated:
        user_clicker = models.Clicker.objects.get(user=request.user)
        return render(request, 'clicker/clicker.html', {'clicker': user_clicker})
    return redirect('home')


def login(request):
    if request.method == 'POST':
        user_name = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('clicker')
    return render(request, 'clicker/login.html')


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save()
            clicker = models.Clicker()
            clicker.user = user
            clicker.save()
            return redirect('login')
        else:
            return render(request, 'clicker/register.html', {'form': form})
    form = RegForm()
    return render(request, 'clicker/register.html', {'form': form})


def stat(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_clicker = models.Clicker.objects.get(user=request.user)
            data = json.load(request)
            user_clicker.blood_score = data["score"]
            user_clicker.click_power = data["power"]
            user_clicker.save()
            return JsonResponse(data=data)


def logout(request):
    auth.logout(request)
    return redirect('home')
