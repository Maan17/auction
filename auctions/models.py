from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

CHOICES =( 
    ("1", "Fashion"), 
    ("2", "Toys"), 
    ("3", "Electronics"), 
    ("4", "Home"),
    ("5", "Edible"),
) 
  

class User(AbstractUser):
    pass


class listing(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    active=models.BooleanField(default="True")
    winner=models.CharField(max_length=64,default="")
    initial_amt=models.IntegerField()
    image=models.ImageField(upload_to='product')
    category=models.CharField(max_length = 20, choices =CHOICES)
    def __str__(self):
        return f"Item ID: {self.id} | Title: {self.title}"

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(listing, on_delete=models.CASCADE,null=True)
    amount=models.IntegerField()
    def __str__(self):
        return f"Item: {self.item} | User: {self.user}"

class comment(models.Model):
    pass             

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(listing)
    def __str__(self):
        return f"{self.user}'s WatchList"