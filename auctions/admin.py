from django.contrib import admin
from .models import bid,User,listing,comment
# Register your models here.
admin.site.register(bid)
admin.site.register(User)
admin.site.register(listing)
admin.site.register(comment)