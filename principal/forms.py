from .models import *
from django import forms


# class ImagemTopoForm(forms.ModelForm):
#     class Meta:
#         model = Topo
#         fields = '__all__'


class ImagenCaroucel1(forms.ModelForm):
    class Meta:
        model = Carousel1
        fields = '__all__'


class ImagenCaroucel2(forms.ModelForm):
    class Meta:
        model = Carousel2
        fields = '__all__'


class ImagenCaroucel3(forms.ModelForm):
    class Meta:
        model = Carousel3
        fields = '__all__'


class ImagenLateralForm(forms.ModelForm):
    class Meta:
        model = ImagemLateral
        fields = '__all__'


class ImagenDestaqueForm(forms.ModelForm):
    class Meta:
        model = ImagensDestaque
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('url',)

class ImagenTabsInfoForm(forms.ModelForm):
    class Meta:
        model = TabsInfo
        fields = '__all__'

    
class ImagenTabsPalestrasForm(forms.ModelForm):
    class Meta:
        model = TabsPalestras
        fields = '__all__'

class ImagenTabsContatoForm(forms.ModelForm):
    class Meta:
        model = TabsContato
        fields = '__all__'


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = '__all__'
