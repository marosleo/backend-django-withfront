from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save


class Cachorro(models.Model): #cards dos cachorros
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
     

    def __str__(self):
        return self.nome
  

class Comedouro(models.Model):
    local = models.CharField(max_length=100)
    hardware = models.CharField(max_length=100)

    def __str__(self):
        return self.local

class Tag(models.Model):
    local  = models.ForeignKey(Comedouro,on_delete=models.PROTECT)
    cachorro = models.ForeignKey(Cachorro,on_delete=models.PROTECT)
    hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cachorro.nome

class Publicacoes(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    publicado = publicado = models.DateTimeField(default=timezone.now)
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo



