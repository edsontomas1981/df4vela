from django.db import models

class Enderecos (models.Model):
    cep=models.CharField(max_length=8,null=False)
    logradouro=models.CharField(max_length=50,null=False)
    numero=models.CharField(max_length=8)
    bairro=models.CharField(max_length=30)
    cidade=models.CharField(max_length=50)
    uf=models.CharField(max_length=2)

