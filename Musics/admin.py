from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Artists , Musics
@register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    pass
@register(Musics)
class MusicsAdmin(admin.ModelAdmin):
    pass