from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
