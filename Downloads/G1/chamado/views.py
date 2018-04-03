from django.shortcuts import render
from .models import Atendimento, Chamado, Funcionario
from django.http import HttpResponse

def chamado(request):
    tipoo = Chamado.objects.all()
    html = '<h1>Chamado</h1>'
    for tipo in tipoo:
        html += '<li>' + '<b>codChamado</b>: ' + tipo.codChamado + ' </b>' + '<b>titulo: </b>' + str(
            tipo.titulo) + '<b> dataAbertura: </b>' + tipo.dataAbertura + '</li>'
    return HttpResponse(html)

def ChamadosIdFuncionario(request, id):
    try:
        tipo = Funcionario.objects.get(id=id)
        html = '<h1>Pessoa por ID</h1>'
        html+= '<li>' + '<b>nome</b>: '+tipo.nome+ ' </b>' + '<b>Email: </b>'+ str(tipo.email)+' <b>numeroChamado: </b>'+ str(tipo.chamados)+'</li>'
        return HttpResponse(html)
    except Exception:
        return HttpResponse('<h1>Pessoa não existe!</h1>')

def ChamadosConcluidos(request):
    tipoo = Chamado.objects.all()
    html = '<h1>Chamados Concluídos</h1>'
    for tipo in tipoo:
            if tipo.status == 'Concluído':
                html += '<li>' + '<b>codChamado</b>: ' + tipo.codChamado + ' </b>' + '<b>titulo: </b>' + str(tipo.titulo) + '<b> dataAbertura: </b>' + tipo.dataAbertura +'</li>'
    return HttpResponse(html)
