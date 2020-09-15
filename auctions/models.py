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
    initial_amt=models.IntegerField()
    image=models.ImageField(upload_to='product')
    category=models.CharField(max_length = 20, choices =CHOICES)
    def __str__(self):
        return f"Item ID: {self.id} | Title: {self.title}"

class bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    item = models.ManyToManyField(listing)
    amount=models.IntegerField(default=0)

class comment(models.Model):
    pass             

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(listing)
    def __str__(self):
        return f"{self.user}'s WatchList"