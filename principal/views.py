from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def home(request):
    
    b_topo = Topo.objects.all().order_by('-id')[:1] 

    carousel1 = Carousel1.objects.all().order_by('-id')[:1]
    carousel2 = Carousel2.objects.all().order_by('-id')[:1]
    carousel3 = Carousel3.objects.all().order_by('-id')[:1]

    imgs_lateral1 = ImagemLateral.objects.all().order_by('-id')[:2]
    
    imagemsDestaque = ImagensDestaque.objects.all().order_by('-id')[:2]

    videos = Video.objects.all().order_by('-id')[:2]

    tabinfos = TabsInfo.objects.all().order_by('-id')[:1]
    tabpalestras = TabsPalestras.objects.all().order_by('-id')[:1]
    tabcontatos = TabsContato.objects.all().order_by('-id')[:1]
   
    context = {
        'b_topo': b_topo,
        'carousel1': carousel1,
        'carousel2': carousel2,
        'carousel3': carousel3,
        'imgs_lateral1': imgs_lateral1,
        'imagemsDestaque': imagemsDestaque,
        'videos': videos,
        'tabinfos': tabinfos,
        'tabpalestras': tabpalestras,
        'tabcontatos': tabcontatos,
        
    }

    return render(request, 'base.html', context)


@login_required()
def home_adm(request):
    return render(request, 'adm/principal_adm.html')