# GoodShare

### Inspiration

While there are many contributing factors to climate change and the detriment of our planet, excess waste is one of the main factors that have been affecting us for a very long time. Not only is the production of waste creating more waste, the “attempted” elimination of waste causes a bigger issue.
 
Waste doesn’t truly get eliminated. It only gets burned, burried, or thrown into the ocean. And this doesn’t  solve the problem, it only makes it worse by now affecting the air we breathe, the water we drink, and the soil that nourishes us. To counter this, we thought what better way to eliminate waste than to just use it? After all, “one mans trash is another man’s treasure”.

### What it does?

GoodShare is a webapp that allows you to post any unwanted goods ranging from nearly expiring food to random reusable items around your house. It allows users to scroll through posts in their area or search for specific needs that they want to find like unique antiques or yummy food up for grabs. Through this, you are able to get rid of your waste without the environmentally detrimental effects that come with simply just throwing it away; not to mention the added bonus of being able to help someone in need and responsibily disposing your “trash”. 

To get involved, all you need is an account. No credit card or payment service needed. This way, we are able bring together community members without any discrimination or financial boundaries all while promoting sustainability and environmentalism. 

### How we built it?

* We built this web app using Pythons Django framework for web development.
* We used Django’s inbuilt user creation and authentication features for user management.
* In addition, we used HTML, CSS and JS to create all the webpages which were made responsive to all screen sizes using Bootstrap.
* Mapquest API and Google Place search APIs were used to find Latitude and Longitude based on address fields, to determine the closest available items.

### What's next?
We can integrate our application with Facebook Marketplace and Craigslist to have unified giveaway online platform.

## Application Flow
* Login is our goto link of webapp. Click Register for first time registration.

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/LoginPage.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/UserRegistration.png" alt="BFS" width="300" height="200">

* Select whether you want to giveaway items or looking for used items:

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/Home.png" alt="BFS" width="300" height="200">

* To create a post choose 'Giveaway', select categories for posting and create a post:

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/Post.png" alt="BFS" width="300" height="200">

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/Foodpost.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/ClothesPost.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/ItemsPost.png" alt="BFS" width="300" height="200">

* Similarly to search nearby item pickups choose 'Pickup' and find giveaway postings using options:

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/Pickup.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/FoodPickup.png" alt="BFS" width="300" height="200">

* Your nearby postings are shown:

<img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/FoodResults.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/ClothesResults.png" alt="BFS" width="300" height="200">  <img src="https://github.com/nikhilchaudhary0126/goodshare/blob/main/outputs/Household%20Results.png" alt="BFS" width="300" height="200">


## Running Instructions

### Requirements
Python3 with ```django``` and ```requests``` module.

### Running instructions 
* To run clone repository using
```git clone <repository link>```
* Run using below command in base directory
```python3 manage.py runserver```


