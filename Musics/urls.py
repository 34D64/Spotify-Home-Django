from django.contrib import admin
from django.urls import path, include
from .views import MusicList


urlpatterns = [
    # path("allmusic/",MusicList.as_view() ),
    path("",MusicList),
    # path("artistMusic/", ),

]