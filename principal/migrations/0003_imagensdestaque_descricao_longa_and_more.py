# Generated by Django 4.2.4 on 2023-08-10 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_remove_imagensdestaque_descricao_longa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagensdestaque',
            name='descricao_longa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='imagensdestaque',
            name='descricao_pequena',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
