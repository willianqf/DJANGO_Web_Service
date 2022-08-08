# IMPORTAR A CLASSE CREATE VIEW DO DJANGO
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# IMPORTAR OS MODELOS DE CLASSES DO BANCO
from .models import Campo, Atividade

# METODO DE DIRECIONAMENTO
from django.urls import reverse_lazy
# Create your views here.

#################### CREATE VIEW ###################################
class CampoCreate(CreateView):
    model = Campo
    fields = ["nome", "descricao"] #QUAIS CAMPOS VOCÊ VAI CRIAR <PRECISA UTILIZAR OS MESMOS DO BANCO>
    template_name = 'cadastros/form.html' #QUAL TEMPLATE VOCÊ USARÁ? INDEX.HTML
    success_url = reverse_lazy('inicio') # URL CASO A CRIAÇÃO OCORRA BEM (reverse_lazy('campo da urls'))

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'foreignkey_campo']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('inicio')

################### UPDATE VIEW #####################################

class CampoUpdate(UpdateView):
    model = Campo
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'foreignkey_campo']
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('inicio')

################### DELETE VIEW #####################################

class CampoDelete(DeleteView):
    model = Campo
   # fields = ["nome", "descricao"]
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

class AtividadeDelete(DeleteView):
    model = Atividade
   # fields = ['numero', 'descricao', 'pontos', 'detalhes', 'foreignkey_campo']
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy('inicio')
