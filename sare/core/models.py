from django.db import models
from sare.questionarios.choices import *
from sare.questionarios.validators import cpf_is_digits, cpf_is_valid


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', unique=True, max_length=14, validators=[cpf_is_digits, cpf_is_valid])
    email = models.EmailField('e-mail')
    fone = models.CharField('telefone', max_length=20, blank=True)
    sexo = models.CharField('sexo', max_length=1, choices=SEXO_CHOICES, default=None)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    endereco = models.CharField('endereço', max_length=100, default=None)
    num_casa = models.CharField('número da casa', max_length=4, default=0)
    cep = models.CharField('cep', max_length=9, default=None)
    bairro = models.CharField('bairro', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    estado = models.CharField('estado', max_length=2, default='TO')

    class Meta:
        verbose_name_plural = 'endereços'
        verbose_name = 'endereço'


class Aluno(Pessoa):
    curso = models.CharField('curso', choices=CURSO_CHOICE.items(), max_length=50, default=None)
    sem_mod_ano = models.CharField('Semestre/Módulo/Ano', max_length=10, default=None)
    matricula = models.CharField('matrícula', max_length=15, default=None)
    campus = models.CharField('campus', max_length=30, default='PALMAS')

    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'