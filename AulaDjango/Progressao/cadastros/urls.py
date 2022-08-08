from django.urls import path

from .views import CampoCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete

urlpatterns = [
    #path('endereço', MinhaView.as_view(), name='nome da url')
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),

    ################# EDITAR REGISTROS #############<int:pk> - PEGA ID CHAVE PRIMÁRIA##################
    ## É necessário chamar pela chave primária
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),

    ################# EXCLUIR REGISTRO #############<int:pk> - PEGA ID CHAVE PRIMÁRIA##################
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade")

]