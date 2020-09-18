from django import forms
from .models import listing,Bid

class listingForm(forms.ModelForm):
    class Meta:
        model=listing
        fields=('title','desc','initial_amt','image','category')

class BidForm(forms.ModelForm):
    class Meta:
        model=Bid
        fields=('amount',)