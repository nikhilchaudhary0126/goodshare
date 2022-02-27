from urllib.request import urlretrieve

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

import os
import requests
import json
from datetime import datetime
from django.shortcuts import render
from giveaway.models import Food, Clothes, HouseholdItems
from giveaway.forms import FoodForm, ClothesForm, HouseholdItemsForm
from django.contrib import messages
from goodshare.settings import API_KEY, MAP_URL


@login_required
def foodPostRequest(request):
    if request.method == "POST":
        try:
            foodtype = request.POST['type']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            quantity = request.POST['quantity']
            expiry = request.POST['expiry']
            contactno = request.POST['contactno']
            description = request.POST['description']
            form = FoodForm(request.POST, request.FILES)
            if form.is_valid():
                if expiry and datetime.strptime(expiry, "%Y-%m-%d") > datetime.now():
                    if foodtype and address and city and state and quantity and contactno:
                        combinedAddress = address + "," + city + "," + state
                        data = getLongLat(combinedAddress)
                        longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
                        latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']

                        f = Food(address=address, city=city, state=state, type=foodtype, latitude=latitude,
                                 longitude=longitude, expiry=expiry, quantity=quantity, contactno=contactno,
                                 description=description)
                        f.save()
                        postid = f.id

                        files = request.FILES.getlist('file')
                        fs = FileSystemStorage()
                        for file in files:
                            path = os.path.join("foodpost", str(postid), file.name)
                            fs.save(path, file)
                        mappath = os.path.join("media", "foodpost", str(postid))
                        curpath = os.getcwd()
                        os.chdir(mappath)
                        urlretrieve(data['results'][0]['locations'][0]['mapUrl'], "map.jpg")
                        os.chdir(curpath)
                        return redirect('home_div')
                    else:
                        messages.error(request, "Food Post failed! Please enter all details.")
                else:
                    messages.error(request, "Food Post failed! Please select a future expiry date")
        except:
            return redirect('home_div')
    return render(request, 'foodPost.html', {"form": FoodForm})


def getLongLat(address: str) -> (int, int):
    parameters = {
        "key": API_KEY,
        "location": address
    }
    response = requests.get(MAP_URL, params=parameters)
    data = json.loads(response.text)
    return data


@login_required
def clothesPostRequest(request):
    if request.method == "POST":
        try:
            print(request.POST)
            description = request.POST['description']
            size = request.POST['size']
            gender = request.POST['gender']
            condition = request.POST['condition']
            contactno = request.POST['contactno']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pickupDate = request.POST['pickupdate']

            if pickupDate and datetime.strptime(pickupDate, "%Y-%m-%d") > datetime.now():
                if size and gender and city and state and address and contactno and condition:
                    combinedAddress = address + "," + city + "," + state
                    data = getLongLat(combinedAddress)
                    longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
                    latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']

                    f = Clothes(size=size, gender=gender, condition=condition, address=address, city=city, state=state,
                                latitude=latitude, longitude=longitude, pickupdate=pickupDate, contactno=contactno,
                                description=description)
                    f.save()
                    postid = f.id

                    files = request.FILES.getlist('file')
                    fs = FileSystemStorage()
                    for file in files:
                        path = os.path.join("clothpost", str(postid), file.name)
                        fs.save(path, file)
                    mappath = os.path.join("media", "clothpost", str(postid))
                    curpath = os.getcwd()
                    os.chdir(mappath)
                    urlretrieve(data['results'][0]['locations'][0]['mapUrl'], "map.jpg")
                    os.chdir(curpath)
                    return redirect('home_div')
                else:
                    messages.error(request, "Clothes Post failed! Please enter all details.")
            else:
                messages.error(request, "Clothes Post failed! Please select a future expiry date")
        except:
            return redirect('home_div')
    return render(request, 'clothPost.html', {"form": ClothesForm})


@login_required
def itemsPostRequest(request):
    if request.method == "POST":
        # try:
        print(request.POST)
        type = request.POST['type']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pickupdate = request.POST['pickupdate']
        contactno = request.POST['contactno']
        description = request.POST['description']
        condition = request.POST['condition']

        if pickupdate and datetime.strptime(pickupdate, "%Y-%m-%d") > datetime.now():
            if type and address and city and state and contactno:
                combinedAddress = address + "," + city + "," + state
                data = getLongLat(combinedAddress)
                longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
                latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']

                f = HouseholdItems(address=address, city=city, state=state, type=type, latitude=latitude,
                                   longitude=longitude, pickupdate=pickupdate, contactno=contactno, condition=condition,
                                   description=description)
                f.save()
                postid = f.id

                files = request.FILES.getlist('file')
                fs = FileSystemStorage()
                for file in files:
                    path = os.path.join("itemspost", str(postid), file.name)
                    fs.save(path, file)
                mappath = os.path.join("media", "itemspost", str(postid))
                curpath = os.getcwd()
                os.chdir(mappath)
                urlretrieve(data['results'][0]['locations'][0]['mapUrl'], "map.jpg")
                os.chdir(curpath)
                return redirect('home_div')
            else:
                messages.error(request, "Food Post failed! Please enter all details.")
        else:
            messages.error(request, "Food Post failed! Please select a future expiry date")
    # except:
    #     return redirect('home_div')
    return render(request, 'householdItemsPost.html', {"form": HouseholdItemsForm})
