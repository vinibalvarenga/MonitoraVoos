from django.shortcuts import render

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
