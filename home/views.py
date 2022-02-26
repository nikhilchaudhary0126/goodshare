from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def giveAway(request):
    return render(request, 'giveAway.html')


def pickUp(request):
    return render(request, 'pickup.html')