"""MonitoraVoos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rota import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='areaLogada.html'), name='home'),
    path('crud/', TemplateView.as_view(template_name='crud.html'), name='crud'),
    path('crud/criar-rota', views.RotaCreate.as_view(), name='criar-rota'),
    path('crud/consultar-rotas', views.RotaListView.as_view(), name='consultar-rota'),
    path('crud/consultar-rotas/<int:pk>', views.RotaDetailView.as_view(), name='rota-detail'),
    path('crud/atualizar-rota', views.RotaUpdateListView.as_view(), name='atualizar-rota'),
    path('crud/atualizar-rota/<int:pk>', views.RotaUpdate.as_view(), name='rota-update-form'),
    path('crud/excluir-rota', views.RotaDeleteListView.as_view(), name='excluir-rota'),
    path('crud/excluir-rota/<pk>', views.RotaDelete.as_view(), name='confirmar-excluir-rota'),
    path('geracaoRelatorios/', views.geracaoRelatorios),
    path('monitoramento/', views.monitoramento)
]
