from django.db import models

class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey() # TODO: needs dynamic ContentType 
    #####################################################
    food = models.ForeignKey() # TODO: needs dynamic ContentType   
    order = models.ForeignKey() # TODO: needs dynamic ContentType ?
    #####################################################
    editted = models.BooleanField(default=False, null=False)
    reply_to = models.IntegerField(null=True) # The id of replied comment
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating = models.IntegerField() # TODO: add possible choices or use IntegerChoices x/10
    created_at = models.DateTimeField(auto_now_add=True)
    to = models.ForeignKey() # TODO: needs dynamic type for order and reserve
    
class Complaint(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    restaurant = models.ForeignKey() # TODO: add dynamic type for restaurant
    status = models.CharField() # TODO: add possible choices Pending and Checked?
    respond = models.TextField(null=True) 
