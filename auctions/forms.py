from django import forms
from .models import listing

class listingForm(forms.ModelForm):
    class Meta:
        model=listing
        fields=('title','desc','initial_amt','image','category')