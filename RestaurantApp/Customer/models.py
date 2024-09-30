from django.db import models

class Customer(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD , 'Gold')
    ]
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]
    
    username = models.CharField(max_length=255, primary_key=True, editable=False)
    first_name = models.CharField(max_length=255, null=False, editable=False)
    last_name = models.CharField(max_length=255, null=False, editable=False)
    phone = models.CharField(max_length=11, unique=True, null=False, editable=False)
    email = models.EmailField(max_length=255, null=False, editable=True)
    address = models.CharField(max_length=255, null=True, editable=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, editable=False)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, null=False, editable=True)