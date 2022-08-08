''' Cria padrões de URL '''

##############################################################
from django.views.generic import TemplateView
##############################################################

####### CLASSE (atributo de herança)
class paginaInicial(TemplateView):
    template_name = "paginas/inin.html"

# Create your views here.

class paginaSobre(TemplateView):
    template_name = "paginas/sobre.html"

class paginaLink(TemplateView):
    template_name = "paginas/link.html"