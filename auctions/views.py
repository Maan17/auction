from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import listing
from .forms import listingForm

from .models import User,listing


def index(request):
    infos=listing.objects.all()
    return render(request, "auctions/index.html",{'infos':infos})

def create(request):
    infos=listing.objects.all()
    form = listingForm(request.POST, request.FILES)
    if form.is_valid():
       listing.objects.create(**form.cleaned_data)
       return render(request, "auctions/index.html", {'infos':infos})
    else:
       return render(request, 'auctions/create.html', {'form': form})

def details(request,title):
    detail=get_object_or_404(listing,title=title)
    return render(request,'auctions/details.html',{'info':detail,'title':title })

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def watchlist(request):
    return render(request, "auctions/watchlist.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
