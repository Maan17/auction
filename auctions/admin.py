from django.contrib import admin
from .models import bid,User,listing,comment,Watchlist

class WatchlistAdmin(admin.ModelAdmin):
    filter_horizontal=("item",)

# Register your models here.
admin.site.register(bid)
admin.site.register(User)
admin.site.register(listing)
admin.site.register(comment)
admin.site.register(Watchlist,WatchlistAdmin)