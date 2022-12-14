# Generated by Django 3.2.13 on 2022-11-11 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('periodo', models.IntegerField(verbose_name='período')),
                ('tipo', models.CharField(choices=[('Z', 'dias'), ('S', 'semanas'), ('M', 'meses'), ('A', 'anos')], max_length=1)),
            ],
            options={
                'verbose_name': 'período',
            },
        ),
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=240, verbose_name='descrição')),
                ('subsistema', models.CharField(blank=True, max_length=120, null=True, verbose_name='sub-sistema')),
                ('detalhes', models.TextField(blank=True, null=True)),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.periodo', verbose_name='período')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=240, verbose_name='descrição')),
                ('anexo', models.FileField(blank=True, null=True, upload_to='media/referencia/')),
            ],
            options={
                'verbose_name': 'referência',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=240, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'responsável',
                'verbose_name_plural': 'responsáveis',
            },
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoReferencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alterado_em', models.DateTimeField(auto_now=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('pagina', models.CharField(blank=True, max_length=20, null=True)),
                ('artigo', models.CharField(blank=True, max_length=20, null=True)),
                ('paragrafo', models.CharField(blank=True, max_length=20, null=True)),
                ('detalhes', models.TextField(blank=True, null=True)),
                ('procedimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.procedimento')),
                ('referencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.referencia')),
            ],
            options={
                'verbose_name': 'procedimento referência',
                'verbose_name_plural': 'procedimentos referências',
                'db_table': 'sistema_procedimento_referencias',
            },
        ),
        migrations.AddField(
            model_name='procedimento',
            name='referencias',
            field=models.ManyToManyField(through='sistema.ProcedimentoReferencias', to='sistema.Referencia', verbose_name='referências'),
        ),
        migrations.AddField(
            model_name='procedimento',
            name='responsaveis',
            field=models.ManyToManyField(to='sistema.Responsavel', verbose_name='responsáveis'),
        ),
        migrations.AddField(
            model_name='procedimento',
            name='sistema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.sistema'),
        ),
    ]
