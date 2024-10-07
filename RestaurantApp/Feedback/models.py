from django.db import models

class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey() 
    
    food = models.ForeignKey() 
    order = models.ForeignKey() 
    
    editted = models.BooleanField(default=False, null=False)
    reply_to = models.IntegerField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    to = models.ForeignKey() 
    
class Complaint(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    restaurant = models.ForeignKey() 
    status = models.CharField() 
    respond = models.TextField(null=True) 
