from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def giveAway(request):
    return render(request, 'giveAway.html')


def pickUp(request):
    return render(request, 'pickup.html')

def food(request):
    return render(request, 'food.html')