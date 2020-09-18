from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listings",views.create,name="create_listings"),
    path("details/<int:product_id>",views.details,name="details"),
    path('watchlist',views.watchlist,name="watchlist"),
    path("add-to-watchlist/<int:product_id>", views.watchlist_add, name="watchlist_add"),
    path("delete-from-watchlist/<int:product_id>",views.watchlist_del,name="watchlist_del"),
    path("bid/<int:product_id>",views.bid,name="bid")
]
