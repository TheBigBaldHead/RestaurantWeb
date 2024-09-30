from django.db import models

class Comment(models.Model):
    text = models.TextField()
    customer = models.ForeignKey() # TODO: needs dynamic ContentType 
    food = models.ForeignKey() # TODO: needs dynamic ContentType   
    editted = models.BooleanField(default=False, null=False)
    reply_to = models.IntegerField(null=True, default=NULL) # The id of replied comment
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

class Review(models.Model):
    rating = models.IntegerField() # TODO: add possible choices or use IntegerChoices
    created_at = models.DateTimeField(auto_now_add=True)
    