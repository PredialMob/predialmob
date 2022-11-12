# Generated by Django 3.2.13 on 2022-11-11 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0001_initial'),
        ('edificio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('indice', models.PositiveIntegerField()),
                ('data', models.DateField()),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificio.edificio', to_field='sid')),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.procedimento')),
                ('sistema_edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificio.edificiosistemas', to_field='sid')),
            ],
            options={
                'verbose_name': 'manutenção',
                'verbose_name_plural': 'manutenções',
            },
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('descricao', models.CharField(max_length=240, verbose_name='descrição')),
                ('aberto', models.BooleanField(default=True)),
                ('cor', models.CharField(default='#888888', max_length=9)),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificio.edificio', to_field='sid')),
            ],
            options={
                'verbose_name': 'situação',
                'verbose_name_plural': 'situações',
            },
        ),
        migrations.CreateModel(
            name='ManutencaoLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('data', models.DateField()),
                ('indice', models.PositiveIntegerField()),
                ('notas', models.TextField()),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificio.edificio', to_field='sid')),
                ('manutencao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.manutencao', to_field='sid', verbose_name='manutenção')),
                ('situacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='programa.situacao', to_field='sid')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, to_field='sid')),
            ],
            options={
                'verbose_name': 'log de manutenção',
                'verbose_name_plural': 'logs de manutenção',
            },
        ),
        migrations.CreateModel(
            name='ManutencaoArquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('sid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('descricao', models.CharField(max_length=240, verbose_name='descrição')),
                ('arquivo', models.FileField(upload_to='')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edificio.edificio', to_field='sid')),
                ('manutencao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programa.manutencaolog', to_field='sid')),
            ],
            options={
                'verbose_name': 'Arquivo de manutenção',
                'verbose_name_plural': 'Arquivos de manutenção',
            },
        ),
        migrations.AddField(
            model_name='manutencao',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='programa.situacao', to_field='sid'),
        ),
    ]
