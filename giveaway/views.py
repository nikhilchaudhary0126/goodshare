from urllib.request import urlretrieve

from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

import os
import requests
import json
from datetime import datetime
from django.shortcuts import render
from giveaway.models import Food
from giveaway.forms import FoodForm
from django.contrib import messages
from goodshare.settings import API_KEY, MAP_URL


def foodPostRequest(request):
    if request.method == "POST":
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

                    f = Food(address=address, city=city, state=state, type=foodtype, latitude=latitude, longitude=longitude,
                             expiry=expiry, quantity=quantity, contactno=contactno, description=description)
                    f.save()
                    print(f)
                    postid = f.id
                    print(postid)

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
    return render(request, 'foodPost.html', {"form": FoodForm})


def getLongLat(address: str) -> (int, int):
    parameters = {
        "key": API_KEY,
        "location": address
    }
    response = requests.get(MAP_URL, params=parameters)
    data = json.loads(response.text)
    return data
