from django.contrib.auth.models import AbstractUser
from django.db import models
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

class bid(models.Model):
    pass

class comment(models.Model):
    pass             