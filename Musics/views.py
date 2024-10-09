from django.shortcuts import render
from .models import Musics , Artists

def MusicList(request):
    context ={}
    qs = Musics.objects.all()
    context['form']= qs
    print(context)
    return render(request,template_name='Home.html',context=context)