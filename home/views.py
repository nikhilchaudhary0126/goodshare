from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import os 



@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def giveAway(request):
    return render(request, 'giveAway.html')

@login_required
def pickUp(request):
    return render(request, 'pickup.html')

def food(request):
    return render(request, 'food.html')

def populate(request):
    return render(request, 'populate.html')

def clothes(request):
    return render(request, 'clothes.html')

def household(request):
    return render(request, 'household.html')

def populateClothes(request):
    return render(request, 'populate-clothes.html')

def checkoutExample(request):
    return render(request, 'checkout-example.html')

def populateHousehold(request):
    return render(request, 'populate-household.html')

