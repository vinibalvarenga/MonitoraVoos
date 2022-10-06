from django.db import models
import datetime
# Create your models here.
class Rota(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=15, null = False, unique = True)
    aeroporto_partida = models.CharField(max_length=200, null=False)
    aeroporto_chegada = models.CharField(max_length=200, null=False)
    hora_partida_prevista= models.TimeField(auto_now=False)
    hora_chegada_prevista= models.TimeField(auto_now=False)
    origem = models.CharField(max_length=20, null=False)
    destino = models.CharField(max_length=20, null=False)
    aeronave = models.CharField(max_length=20, null=False)
    companhia_aerea = models.CharField(max_length=20, null=False)
    class Meta:
        db_table = 'rotas'



class Voo(models.Model):
    STATUS_POSSIVEIS = (
        ('em', 'embarcando'),
        ('ca', 'cancelado'),
        ('pr', 'programado'),
        ('ta', 'taxiando'),
        ('pt', 'pronto'),
        ('ao', 'autorizado'),
        ('vo', 'em_voo'),
        ('at', 'aterrisao')
    )
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE, null=True)
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=2, null=False, choices=STATUS_POSSIVEIS)
    piloto = models.CharField(max_length=20, null=False)
    hora_partida = models.TimeField(auto_now=False)
    hora_chegada = models.TimeField(auto_now=False)
    data = models.DateTimeField(null=True)
    class Meta:
        db_table = 'voos'