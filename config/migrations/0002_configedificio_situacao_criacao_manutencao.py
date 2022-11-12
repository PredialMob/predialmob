# Generated by Django 3.2.13 on 2022-11-11 17:16

import config.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programa', '0001_initial'),
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configedificio',
            name='situacao_criacao_manutencao',
            field=config.models.ConfigForeignKey(blank=True, help_text='edificio.models.pre_save_edificio_sistema', null=True, on_delete=django.db.models.deletion.SET_NULL, to='programa.situacao', verbose_name='Situação para criação automática de manutenção'),
        ),
    ]
