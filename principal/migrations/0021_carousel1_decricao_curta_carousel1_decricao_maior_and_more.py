# Generated by Django 4.2.4 on 2023-08-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_carousel1_carousel2_carousel3_delete_caurosel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel1',
            name='decricao_curta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carousel1',
            name='decricao_maior',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carousel2',
            name='decricao_curta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carousel2',
            name='decricao_maior',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carousel3',
            name='decricao_curta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='carousel3',
            name='decricao_maior',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
