from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django import forms
# from django.contrib.auth.decorators import login_required, permission_required

# from rota.forms import CriarRotaForm
from rota.models import Rota, Voo, RotaForm, RotaUpdateForm, VooFuncionarioForm, VooPilotoForm, VooTorreForm

# Create your views here.
def login(request):
    return render(request,"login.html")

def area_logada(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"area_logada.html", context)

def crud(request):
    return render(request,"crud.html")

def geracao_relatorios(request):
    return render(request,"geracao_relatorios.html")

def monitoramento(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"monitoramento.html", context)

def voos_companhia(request):
    voos = Voo.objects.all()

    freq = {}
    for voo in voos:
        if voo.rota.companhia_aerea in freq:
            freq[voo.rota.companhia_aerea] += 1
        else:
            freq[voo.rota.companhia_aerea] = 1

    
    context = {
        'companhias_aereas': freq,
    }
    return render(request,"geracao_relatorios/voos_companhia.html", context)

def voos_destino(request):
    voos = Voo.objects.all()

    freq = {}
    for voo in voos:
        if voo.rota.destino in freq:
            freq[voo.rota.destino] += 1
        else:
            freq[voo.rota.destino] = 1

    
    context = {
        'destinos': freq,
    }
    return render(request,"geracao_relatorios/voos_destino.html", context)

class MonitoraVoo(UpdateView):
    model = Voo
    template_name = 'monitoramento/status_manager.html'
    success_url = reverse_lazy('monitoramento')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Piloto').exists():
            return VooPilotoForm
        elif self.request.user.groups.filter(name='Torre de Controle').exists():
            return VooTorreForm
        else:
            return VooFuncionarioForm


class RotaCreate(CreateView):
    model = Rota
    form_class = RotaForm
    success_url = reverse_lazy('crud')

class RotaUpdateListView(ListView):
    model = Rota
    template_name = 'crud/atualizar_rota.html'

class RotaUpdate(UpdateView):
    model = Rota
    form_class= RotaUpdateForm
    success_url = reverse_lazy('crud')

class RotaListView(ListView):
    model = Rota

class RotaDetailView(DetailView):
    model = Rota
    template_name = 'crud/consultar_rotas/rota_detail.html'

class RotaDeleteListView(ListView):
    model = Rota
    template_name = 'crud/excluir_rota.html'

class RotaDelete(DeleteView):
    model = Rota
    template_name = 'crud/excluir_rota/confirmar_excluir_rota.html'
    success_url = reverse_lazy('crud')


class VooCreate(CreateView):
    model = Voo
    fields = ['rota', 'id', 'piloto', 'hora_partida', 'hora_chegada', 'data']
    success_url = reverse_lazy('crud')

class VooUpdateListView(ListView):
    model = Voo
    template_name = 'crud/atualizar_voo.html'

class VooUpdate(UpdateView):
    model = Voo
    fields = ['status', 'data', 'hora_partida', 'hora_chegada', 'piloto']
    success_url = reverse_lazy('crud')

class VooListView(ListView):
    model = Voo

class VooDetailView(DetailView):
    model = Voo
    template_name = 'crud/consultar_voos/voo_detail.html'

class VooDeleteListView(ListView):
    model = Voo
    template_name = 'crud/excluir_voo.html'

class VooDelete(DeleteView):
    model = Voo
    template_name = 'crud/excluir_voo/confirmar_excluir_voo.html'
    success_url = reverse_lazy('crud')

