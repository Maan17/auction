from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import listing,Watchlist,Bid,User,Comment,CHOICES
from .forms import listingForm,BidForm,CommentForm
from django.contrib import messages

def index(request):
    infos=listing.objects.filter(active=True).order_by('-published_date')
    for info in infos:
        if Bid.objects.filter(item__id=info.id).exists():             
            maxi=Bid.objects.filter(item__id=info.id).last()
            info.current_price=maxi.amount
        else:
            info.current_price=info.initial_amt
    return render(request, "auctions/index.html",{
        'infos':infos,
        })

def create(request):
    infos=listing.objects.filter(active=True)
    form = listingForm(request.POST, request.FILES)
    if form.is_valid():
        item = form.save(commit=False)
        item.owner = request.user
        item.save()
        return index(request)
    else:
       return render(request, 'auctions/create.html', {'form': form})

def all_listings(request):
    product=listing.objects.all().order_by('-published_date')
    return  render(request,'auctions/all_listings.html',{'product':product})

def categories(request):
    category=CHOICES
    return  render(request,'auctions/categories.html',{
        'category':category,
        })

def category_page(request,category):
    infos=listing.objects.filter(category=category,active=True)
    return  render(request,'auctions/category_page.html',{'infos':infos})

def details(request,product_id):
    detail=get_object_or_404(listing,pk=product_id)
    if Comment.objects.filter(item_id=product_id).exists():
        comm=Comment.objects.filter(item_id=product_id)
    else:
        comm=None
    owner=False
    win=False
    active=False
    if request.user.is_authenticated:
        delete=Watchlist.objects.filter(user=request.user, item=product_id)
        amt=BidForm()
        comment=CommentForm()
        if request.user.username == detail.owner:
            owner=True
        if Bid.objects.filter(item__id=product_id).exists():
            maxi=Bid.objects.filter(item__id=product_id).last()
            current_price=maxi.amount
        else:
            start=get_object_or_404(listing,pk=product_id)
            current_price=start.initial_amt
        if detail.winner == request.user.username:
            win=True
        if detail.active == True:
            active=True
        return render(request,'auctions/details.html',{
        'info':detail,
        'del':delete,
        'amt':amt,
        'current':current_price,
        'owner':owner,
        'win':win,
        'active':active,
        'comm':comm,
        'comment':comment,
        })
    else: 
        return render(request,'auctions/details.html',{
            'info':detail,
            })

def bid(request,product_id):
    listi = listing.objects.get(pk=product_id)
    lis = get_object_or_404(listing,pk=product_id)
    if request.method == "POST":
        bidi = Bid(user=request.user, item=listi)
        bidform = BidForm(request.POST, instance=bidi)        
        if Bid.objects.filter(item__id=product_id).exists():
            maxi=Bid.objects.filter(item__id=product_id).last()
            current_price=maxi.amount
        else:
            current_price=lis.initial_amt
        if bidform.is_valid():
            bidform.save()
            if Bid.objects.filter(item__id=product_id).exists():
                res=Bid.objects.filter(item__id=product_id).last()
                response=res.amount
                if current_price>response:
                    res.delete()
                    less_bid=True
                    messages.error(request, 'Your Bid should be greater than current bid.')
                    return details(request, product_id)
        else:
            bidform=BidForm(instance=bidi)
            return details(request, product_id)
    return HttpResponseRedirect(reverse("details", args=(product_id,)))
    
def add_comment(request,product_id):
    product=get_object_or_404(listing,pk=product_id)
    if request.method=='POST':
        prod=Comment(user=request.user,item=product)
        form=CommentForm(request.POST,instance=prod)
        if form.is_valid():
            comment=form.save()
            comment.user=request.user
            comment.item=product
            comment.save()
            return HttpResponseRedirect(reverse("details", args=(product_id,)))
    else:
        form=CommentForm()
        return details(request, product_id)
    return HttpResponseRedirect(reverse("index", args=(product_id,)))

def watchlist(request):
    current_user_watchlist, created = Watchlist.objects.get_or_create(user = request.user)
    items_in_watchlist = current_user_watchlist.item.all()
    return render(request, "auctions/watchlist.html", {"item": items_in_watchlist})

def watchlist_add(request, product_id):
    item_to_save = get_object_or_404(listing, pk=product_id)
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    user_list.item.add(item_to_save)
    #messages.add_message(request, messages.SUCCESS, "Successfully added to your watchlist")
    return HttpResponseRedirect(reverse("details",args=(product_id,)))

def watchlist_del(request,product_id):
    item_to_del=get_object_or_404(listing, pk=product_id)
    user_list= Watchlist.objects.get(user=request.user)
    user_list.item.remove(item_to_del)
    return HttpResponseRedirect(reverse("details",args=(product_id,)))

def close_bid(request,product_id):
    item_to_close=get_object_or_404(listing, pk=product_id)
    item_to_close.active=False
    win=Bid.objects.filter(item__id=product_id).last()
    win=win.user.username
    item_to_close.winner=win
    item_to_close.save()
    return HttpResponseRedirect(reverse("index"))

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
