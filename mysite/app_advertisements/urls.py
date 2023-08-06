from django.urls import path
from .views import index, top_sellers, advertisement_post, register, login, profile

urlpatterns = [
    path('', index),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement-post/', advertisement_post, name="advertisement_post"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('profile/', profile, name="profile"),






]
