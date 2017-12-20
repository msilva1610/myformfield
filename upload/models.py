from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField('Descrição', max_length=255, blank=True)
    document = models.FileField('Documento', upload_to='documents/')
    uploaded_at = models.DateTimeField('Carregado em', auto_now_add=True)
