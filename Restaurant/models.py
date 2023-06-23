from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=20)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()


class Menu(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    inventory = models.CharField(max_length=200)
