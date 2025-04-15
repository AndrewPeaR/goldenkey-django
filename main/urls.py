from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('sendbook', sendBook, name='sendBook'),
    path('goldenkey', goldenkey, name='goldenkey'),
    path('bashaeva', bashaeva, name='bashaeva'),
    path('review', review, name='review'),
    path('news', news, name='news'),
    path('filial/team', teamFilial, name='teamFilial'),
    path('filial/<slug:filial_slug>', filial, name='filial'),
]