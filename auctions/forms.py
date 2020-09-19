from django import forms
from .models import listing,Bid,Comment

class listingForm(forms.ModelForm):
    class Meta:
        model=listing
        fields=('title','desc','initial_amt','image','category')

class BidForm(forms.ModelForm):
    class Meta:
        model=Bid
        fields=('amount',)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)