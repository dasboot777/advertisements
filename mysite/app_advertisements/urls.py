from django.urls import path
from .views import index, top_sellers, advertisement_post, register, login, profile
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement-post/', advertisement_post, name="advertisement_post"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('profile/', profile, name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


