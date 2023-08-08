from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
@login_required()
def home_adm(request):
    return render(request, 'adm/principal_adm.html')


@csrf_exempt
@login_required()
def AdicionarImagemTopo(request):
    template_name = 'adm/addimagemtopo.html'
    context = {}
    if request.method == 'POST':
        form = ImagemTopoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem do topa adicinada com sucesso.')
            return redirect('principal:home_adm')


    else:
        form = ImagemTopoForm()
    context['form'] = form
    return render(request, template_name, context)


@csrf_exempt
@login_required()
def AdicionarCaroucel1(request):
    template_name = 'adm/adicionarcaroucel1.html'
    context = {}
    if request.method == 'POST':
        form = ImagenCaroucel1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem do carrossel 1 adcionada com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenCaroucel1()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@csrf_exempt
@login_required()
def AdicionarCaroucel2(request):
    template_name = 'adm/adicionarcaroucel2.html'
    context = {}
    if request.method == 'POST':
        form = ImagenCaroucel2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem do carrossel 2 adcionada com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenCaroucel2()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@csrf_exempt
@login_required()
def AdicionarCaroucel3(request):
    template_name = 'adm/adicionarcaroucel3.html'
    context = {}
    if request.method == 'POST':
        form = ImagenCaroucel3(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem do carrossel 3 adcionada com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenCaroucel3()
    context = {
        'form': form,
    }
    return render(request, template_name, context)



@login_required()
def AdicionarImagemLateral(request):
    template_name = 'adm/adicionarimagemlateral.html'
    context = {}
    if request.method == 'POST':
        form = ImagenLateralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem lateral adcionada com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenLateralForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)



@login_required()
def AdicionarImagemDestaque(request):
    template_name = 'adm/adicionarimagemdestaque.html'
    context = {}
    if request.method == 'POST':
        form = ImagenDestaqueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem destaque adcionada com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenDestaqueForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context) 



@login_required()
def AdicionarVideo(request):
    template_name = 'adm/adicionarvideo.html'
    context = {}
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo adcionado com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = VideoForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context) 



@login_required()
def AdicionarTabsInfo(request):
    template_name = 'adm/adicionartabsinfo.html'
    context = {}
    if request.method == 'POST':
        form = ImagenTabsInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo adcionado com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenTabsInfoForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context) 


@login_required()
def AdicionarTabsPalestra(request):
    template_name = 'adm/adicionartabspalestra.html'
    context = {}
    if request.method == 'POST':
        form = ImagenTabsPalestrasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo adcionado com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenTabsPalestrasForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context) 



@login_required()
def AdicionarTabsContato(request):
    template_name = 'adm/adicionartabscontato.html'
    context = {}
    if request.method == 'POST':
        form = ImagenTabsContatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vídeo adcionado com sucesso.')
            return redirect('principal:home_adm')

    else:
        form = ImagenTabsContatoForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context) 



