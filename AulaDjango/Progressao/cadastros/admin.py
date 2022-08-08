from django.contrib import admin
### PRECISA IMPORTAR AS CLASSES ###
from .models import Campo, Atividade

# Register your models here
# REGISTRAR OS MODELOS.

admin.site.register(Campo)
admin.site.register(Atividade)