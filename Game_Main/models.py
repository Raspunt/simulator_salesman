from itertools import product
from django.db import models

    

class Product(models.Model):
    name = models.CharField(max_length=100)
    type_product = models.CharField(max_length=100)
    freshness = models.CharField(max_length=100)
    cost = models.IntegerField()
    weightkg = models.IntegerField()
    

    def __str__(self):
        return self.name

class Dealer(models.Model):
    delerName = models.CharField(max_length=100)
    telegaName = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    money = models.IntegerField() 
    weightkg = models.IntegerField()

    def __str__(self):
        return self.delerName

class City(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    daysToArrivalTelega=models.IntegerField(blank=True)


    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=100)
    Waysted_days = models.IntegerField()


    def __str__(self) :
        return self.title