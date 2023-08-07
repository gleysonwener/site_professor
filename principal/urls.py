from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.home, name='home'),
    path('home_adm/', views.home_adm, name='home_adm'),    
    path('imagem-topo/', views.AdicionarImagemTopo, name='imagem_topo'),    
    path('imagem-caurocel1/', views.AdicionarCaroucel1, name='imagem_caurocel1'),    
    path('imagem-caurocel2/', views.AdicionarCaroucel2, name='imagem_caurocel2'),    
    path('imagem-caurocel3/', views.AdicionarCaroucel3, name='imagem_caurocel3'),    
    path('imagem-lateral/', views.AdicionarImagemLateral, name='imagem_lateral'),    
    path('imagem-destaque/', views.AdicionarImagemDestaque, name='imagem_destaque'),    
    path('video/', views.AdicionarVideo, name='video'),    
    path('imagem-tabs-info/', views.AdicionarTabsInfo, name='tabs_info'),    
    path('imagem-tabs-palestra/', views.AdicionarTabsPalestra, name='tabs_palestra'),    
    path('imagem-tabs-contato/', views.AdicionarTabsContato, name='tabs_contato'),    
]
