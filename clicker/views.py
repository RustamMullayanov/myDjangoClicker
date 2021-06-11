from django.shortcuts import render


def home(request):
    return render(request, 'clicker/home.html')


def login(request):
    return render(request, 'clicker/login.html')


def register(request):
    return render(request, 'clicker/register.html')