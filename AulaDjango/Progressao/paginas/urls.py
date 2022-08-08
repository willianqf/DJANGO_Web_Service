# IMPORTAR AS URLS 
from django.urls import path
#######################################
# IMPORTAR AS CLASSES DE URLS DENTRO DA VIEWS

from .views import paginaInicial, paginaSobre, paginaLink

urlpatterns = [
    #path('endereço', MinhaView.as_view(), name='nome da url')
    path('PaginaInicial/', paginaInicial.as_view(), name='inicio'), #{% url 'name' %}
    path('sobre/', paginaSobre.as_view(), name='Sobre'),
    path('link/', paginaLink.as_view(), name='link')
]