from django.contrib import admin
from .models import Funcionario, Chamado, Atendimento

admin.site.register(Funcionario)
admin.site.register(Chamado)
admin.site.register(Atendimento)


# Register your models here.
