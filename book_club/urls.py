from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='book-home' ),
    path('about/', about, name='book-about' ),
]
