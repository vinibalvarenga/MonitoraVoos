from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django import forms
# from django.contrib.auth.decorators import login_required, permission_required

# from rota.forms import CriarRotaForm
from rota.models import Rota, Voo

# Create your views here.
def login(request):
    return render(request,"login.html")

def areaLogada(request):
    return render(request,"areaLogada.html")

def crud(request):
    return render(request,"crud.html")

def geracaoRelatorios(request):
    return render(request,"geracaoRelatorios.html")

def monitoramento(request):
    voos = Voo.objects.all()
    context = {
        'voos': voos,
    }
    return render(request,"monitoramento.html", context)

class MonitoraVoo(UpdateView):
    model = Voo
    fields = ['status']
    template_name = 'monitoramento/status_manager.html'
    success_url = reverse_lazy('monitoramento')


class RotaCreate(CreateView):
    model = Rota
    fields = '__all__'
    success_url = reverse_lazy('crud')

class RotaUpdateListView(ListView):
    model = Rota
    template_name = 'crud/atualizar_rota.html'

class RotaUpdate(UpdateView):
    model = Rota
    fields = ['aeronave', 'hora_partida_prevista', 'hora_chegada_prevista']
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
    fields = '__all__'
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

