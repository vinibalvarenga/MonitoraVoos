# Generated by Django 4.1.1 on 2022-10-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=15, unique=True)),
                ('aeroporto_partida', models.CharField(max_length=200)),
                ('aeroporto_chegada', models.CharField(max_length=200)),
                ('hora_partida_prevista', models.DateTimeField()),
                ('hora_chegada_prevista', models.DateTimeField()),
                ('origem', models.CharField(max_length=20)),
                ('destino', models.CharField(max_length=20)),
                ('aeronave', models.CharField(max_length=20)),
                ('companhia_aerea', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rotas',
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('em', 'embarcando'), ('ca', 'cancelado'), ('pr', 'programado'), ('ta', 'taxiando'), ('pt', 'pronto'), ('ao', 'autorizado'), ('vo', 'em_voo'), ('at', 'aterrisao')], max_length=2)),
                ('piloto', models.CharField(max_length=20)),
                ('hora_partida', models.DateTimeField()),
                ('hora_chegada', models.DateTimeField()),
                ('data', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'voos',
            },
        ),
    ]
