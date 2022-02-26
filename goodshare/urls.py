"""goodshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login import views as loginApp
from home import views as homeApp

from search import views as searchApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginApp.userlogin, name='login'),
    path('search/', searchApp.test, name='search'),
    path('login', loginApp.userlogin, name='login'),
    path('register/', loginApp.register_request),
    path('home/', homeApp.home, name='home_div'),
    path('give_away/', homeApp.giveAway, name='give_away'),
    path('pickup/', homeApp.pickUp, name='pickup'),
    path('food_pickup/', homeApp.food, name='food'),
    path('populate/', homeApp.populate, name='populate'),
]


