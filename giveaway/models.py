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
