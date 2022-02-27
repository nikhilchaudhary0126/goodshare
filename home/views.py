from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def giveAway(request):
    return render(request, 'giveAway.html')

@login_required
def pickUp(request):
    return render(request, 'pickup.html')