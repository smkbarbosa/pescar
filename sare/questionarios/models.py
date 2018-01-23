from django.db import models

# Create your models here.
class Questionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    SEX_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)