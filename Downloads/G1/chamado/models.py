from django.db import models

class Chamado(models.Model):
    codChamado = models.CharField('codChamado', max_length=20)
    titulo = models.CharField('titulo', max_length=50)
    descricao = models.TextField('descricao')
    telefoneSolicitante = models.CharField('telefoneSolicitante', max_length=20)
    departamentoSolicitante = models.CharField('departamentoSolicitante', max_length=50)
    dataAbertura = models.CharField('dataAbertura', max_length=20)
    status = models.CharField('status', max_length=50)
    visibilidade = (('publico', 'Público'), ('privado', 'Privado'))
    visivel = models.CharField('visivel', max_length=50, choices=visibilidade, default='Privado')
    categoria = models.CharField('categoria', max_length=50)

    def __str__(self):
        return self.codChamado

class Funcionario(models.Model):
    chamados = []
    nome = models.CharField('nome', max_length=100)
    email = models.CharField('email', max_length=100)
    chamados = models.ForeignKey(Chamado, 'chamado', blank=True, null=True)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    funcionariosAtendimento = []
    descricao = models.TextField('descricao')
    funcionariosAtendimento = models.ForeignKey(Funcionario, 'funcionarioAtendimento', blank=True, null=True)

    def __str__(self):
        return self.funcionariosAtendimento