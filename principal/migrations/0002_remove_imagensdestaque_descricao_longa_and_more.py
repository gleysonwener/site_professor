# Generated by Django 4.2.4 on 2023-08-10 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagensdestaque',
            name='descricao_longa',
        ),
        migrations.RemoveField(
            model_name='imagensdestaque',
            name='descricao_pequena',
        ),
    ]
