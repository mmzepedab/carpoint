# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('estado_caso_id', models.IntegerField(choices=[(1, 'Iniciado'), (2, 'En Proceso'), (3, 'Completado')], default=1)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]