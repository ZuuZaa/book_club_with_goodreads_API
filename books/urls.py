from django.urls import path
from .views import *
from .cron import replace

urlpatterns = [
    path('nextbook/', vote_page, name = 'vote_page'),
    path('nextbook/search/', search, name = 'search'),
    path('nextbook/choose/', choose_book, name = 'choose_book'),
    path('nextbook/<int:b_id>/', vote, name = 'votebook'),
    path('replacement/', replace),
    path('read/<int:id>/', readen, name = 'readen'),
    path('nextbook/archive/', archive, name = 'archive'),
]
