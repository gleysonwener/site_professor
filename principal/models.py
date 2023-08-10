from django.db import models

from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()
        

# class Topo(models.Model):
#     banner_topo = models.ImageField(upload_to='static/imagens', blank=True, null=True)

#     def __str__(self):
#         return str(self.banner_topo)
    

class TabsInfo(models.Model):

    tabsinfo = models.ImageField(upload_to="static/imagens",blank=True, null=True)
   

    def __str__(self):
        return str(self.tabsinfo)
    

class TabsPalestras(models.Model):

    tabspalestra = models.ImageField(upload_to="static/imagens",blank=True, null=True)
   

    def __str__(self):
        return str(self.tabspalestras)
       


class TabsContato(models.Model):

    tabscontato = models.ImageField(upload_to="static/imagens",blank=True, null=True)
   

    def __str__(self):
        return str(self.tabscontato)
    

class ImagemLateral(models.Model):

    img_1 = models.ImageField(upload_to='static/imagens', blank=True, null=True)
   

    def __str__(self):
        return str(self.img_1)
    

class Video(models.Model):

    dt_upload = models.DateTimeField(auto_now_add=True,  blank=True, null=True)
    url = EmbedVideoField( blank=True, null=True)


    def __str__(self):
        return str(self.url)


class ImagensDestaque(models.Model):

    imgDestaque1 = models.ImageField(upload_to='static/imagens', blank=True, null=True)
    descricao_pequena = models.CharField(max_length=25, blank=True, null=True)
    descricao_longa = models.CharField(max_length=100, blank=True, null=True)
    
    
    def __str__(self):
        return str(self.imgDestaque1)
    

class Carousel1(models.Model):
       carousel1 = models.ImageField(upload_to="static/imagens", blank=True, null=True)
       decricao_curta = models.CharField(max_length=50, blank=True, null=True)
       decricao_maior = models.CharField(max_length=100, blank=True, null=True)

       def __str__(self):
        return str(self.carousel1)
    

class Carousel2(models.Model):

       carousel2 = models.ImageField(upload_to="static/imagens", blank=True, null=True)
       decricao_curta = models.CharField(max_length=50, blank=True, null=True)
       decricao_maior = models.CharField(max_length=100, blank=True, null=True)
       

       def __str__(self):
            return str(self.carousel2)

class Carousel3(models.Model):

       carousel3 = models.ImageField(upload_to="static/imagens", blank=True, null=True)
       decricao_curta = models.CharField(max_length=50, blank=True, null=True)
       decricao_maior = models.CharField(max_length=100, blank=True, null=True)


       def __str__(self):
            return str(self.carousel3)
       

class Contato(models.Model):
    assunto = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    texto = models.TextField()
