from django.urls import path
from .views import chamado, ChamadosIdFuncionario, ChamadosConcluidos
urlpatterns = [
    path('chamado', chamado, name='chamado'),
    path('', chamado, name='chamado'),
    path('usuario/<int:id>', ChamadosIdFuncionario, name='chamadosIdFuncionario'),
    path('chamados/concluidos', ChamadosConcluidos, name='ChamadosConcluidos'),
]