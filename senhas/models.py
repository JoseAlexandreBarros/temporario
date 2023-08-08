from django.db import models

class Dados(models.Model):
    nome=models.CharField(max_length=50,default='nome')
    e_mail=models.CharField(max_length=70,default='mail')
    senha=models.CharField(max_length=50,default='senha')
    codigo=models.CharField(max_length=5,default='nulo')
    ativado=models.BooleanField(default=False)
    logado=models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome
