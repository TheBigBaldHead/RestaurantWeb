from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255) # TODO: wrong field
    price = models.IntegerField()
    picture = models.URLField(null=True) # TODO: need parameters?
    inventory = models.PositiveIntegerField(null=True, default=0) 
    
class Reserve(models.Model):
    pass

class Order(models.Model):
    pass

class Cart(models.Model):
    pass