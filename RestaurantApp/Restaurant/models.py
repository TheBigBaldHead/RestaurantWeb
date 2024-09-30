from django.db import models

class Restaurant(models.Model):
    pass

class Food(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255) # TODO: wrong field
    price = models.IntegerField()
    picture = models.URLField(null=True) # TODO: need parameters?
    inventory = models.PositiveIntegerField(null=True, default=0) 
    
class Reserve(models.Model):
    duration = models.PositiveIntegerField() # TODO: add choices
    penalty = models.PositiveIntegerField() # TODO: add choices or models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    pass

class Membership(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze', ),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD , 'Gold')
    ]
    
    Memberships = {
        MEMBERSHIP_BRONZE: {'Price': 100000, 'Reserves': 2 },
        MEMBERSHIP_SILVER: {'Price': 150000, 'Reserves': 5 },
        MEMBERSHIP_GOLD  : {'Price': 300000, 'Reserves': 15},
    }
    
    created_at = models.DateTimeField(auto_now_add=True)
    remaining_reserves = models.IntegerField() # TODO: add parameters
    