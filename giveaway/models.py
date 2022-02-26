from django.db import models


class Food(models.Model):
    expiry = models.DateTimeField()
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(max_length=20)
    quantity = models.CharField(max_length=5)
    contactno = models.IntegerField()
    description = models.CharField(max_length=250)

class Clothes(models.Model):
    size = models.CharField(max_length=10)
    condition = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)
    contactno = models.IntegerField()
    description = models.CharField(max_length=250)

class Items(models.Model):
    pass