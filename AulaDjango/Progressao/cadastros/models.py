from django.db import models

# Create your models here.
# int = IntegerField
# float = FloatField / DecimalField
# string = CharField
#
# OBS: PRECISA PEDIR PARA O DJANGO CRIAR AS TABELAS NO BANCO DE DADOS 
# COMANDO: python manage.py makemigrations
#          python manage.py migrate


class Campo(models.Model):
    nome = models.CharField(max_length=50) # CRIA UM ATRIBUTO NA TABELA DO TIPO CharField (max de letras)
    descricao = models.CharField(max_length=150, verbose_name="Descrição") #verbose_name="Subistitui o nome da variavel por este"

    def __str__(self): #Função executada na parte de demostração dos campos /admin
        return "{} -{}- ({})".format(self.pk, self.nome, self.descricao)

#################################################################################################

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descrição") #max_length -> máximo de caracteristicas
    pontos = models.DecimalField(decimal_places=1, max_digits=4) #decimal_places -> digitos decimais / max_digits -> máximo de digitos
    detalhes = models.CharField(max_length=100)

    #CHAVE ESTRANGEIRAS
    foreignkey_campo = models.ForeignKey(Campo, on_delete=models.PROTECT) #ForeignKey chave estrangeira ('classe que vai ligar', 'Tipo de regra')
    
    def __str__(self): #Função executada na parte de demostração dos campos /admin
        return "{} _ {} - {} ({})".format(self.pk, self.numero, self.descricao, self.foreignkey_campo.nome)
