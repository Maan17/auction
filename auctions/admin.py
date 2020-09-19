from django.contrib import admin
from .models import Bid,User,listing,Comment,Watchlist

class WatchlistAdmin(admin.ModelAdmin):
    filter_horizontal=("item",)


# Register your models here.
admin.site.register(Bid)
admin.site.register(User)
admin.site.register(listing)
admin.site.register(Comment)
admin.site.register(Watchlist,WatchlistAdmin)