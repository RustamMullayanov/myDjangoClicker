from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clicker', clicker, name='clicker'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('stat', stat, name='stat')
]


