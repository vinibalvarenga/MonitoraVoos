from django.db import models
from django.forms import ModelForm
from django import forms
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

    def __str__(self):
        return self.codigo

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
    hora_partida = models.TimeField(auto_now=False, null=True)
    hora_chegada = models.TimeField(auto_now=False, null=True)
    data = models.DateTimeField(null=True)
    class Meta:
        db_table = 'voos'


class RotaForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Rota    
 
        # Custom fields
        fields = '__all__'
 
    # this function will be used for the validation
    def clean(self):

        super(RotaForm, self).clean()

        hora_partida_prevista = self.cleaned_data.get('hora_partida_prevista')
        hora_chegada_prevista = self.cleaned_data.get('hora_chegada_prevista')
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        aeroporto_partida = self.cleaned_data.get('aeroporto_partida')
        aeroporto_chegada = self.cleaned_data.get('aeroporto_chegada')

        if hora_partida_prevista > hora_chegada_prevista:
            self._errors['hora_chegada_prevista'] = self.error_class([
                'Hora de chegada deve ser maior que hora de partida'])

        if origem == destino:
            self._errors['destino'] = self.error_class([
                'Destino deve ser diferente de origem'])

        if aeroporto_chegada == aeroporto_partida:
            self._errors['aeroporto_partida'] = self.error_class([
                'Aeroporto destino deve ser diferente do aeroporto de origem'])

        if aeroporto_chegada != "Guarulhos" and aeroporto_partida != "Guarulhos":
            self._errors['aeroporto_partida', 'aeroporto_chegada'] = self.error_class([
                'Origem ou destino deve ser o aeroporto de Guarulhos'
            ])

        if origem != "São Paulo" and destino != "São Paulo":
            self._errors['origem', 'destino'] = self.error_class([
                'Origem ou destino deve ser São Paulo'
            ])
            self._errors['destino'] = self.error_class([
                'Origem ou destino deve ser São Paulo'
            ])

        return self.cleaned_data


class RotaUpdateForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Rota    
 
        # Custom fields
        fields = ['aeronave', 'hora_partida_prevista', 'hora_chegada_prevista']
 
    # this function will be used for the validation
    def clean(self):

        super(RotaUpdateForm, self).clean()

        hora_partida_prevista = self.cleaned_data.get('hora_partida_prevista')
        hora_chegada_prevista = self.cleaned_data.get('hora_chegada_prevista')


        if hora_partida_prevista > hora_chegada_prevista:
            self._errors['hora_chegada_prevista'] = self.error_class([
                'Hora de chegada deve ser maior que hora de partida'])

        return self.cleaned_data
