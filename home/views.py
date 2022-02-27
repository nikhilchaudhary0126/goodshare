from django.shortcuts import render
import os 

def home(request):
    return render(request, 'home.html')


def giveAway(request):
    return render(request, 'giveAway.html')


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

