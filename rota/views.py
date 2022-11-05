from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required, permission_required

# from rota.forms import CriarRotaForm
from rota.models import Rota

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
    return render(request,"monitoramento.html")

def get_rotas(request):
    return render(request,"crud/consultar-rotas.html")

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
    template_name = 'crud/consultar-rotas/rota_detail.html'

class RotaDeleteListView(ListView):
    model = Rota
    template_name = 'crud/excluir_rota.html'

class RotaDelete(DeleteView):
    model = Rota
    template_name = 'crud/excluir_rota/confirmar_excluir_rota.html'
    success_url = reverse_lazy('crud')



def buscar_rota(request):
    if request.method == "POST":
        searched = request.POST['searched']
        rota = Rota.objects.filter(name__contains==searched)
    return render(request, '')