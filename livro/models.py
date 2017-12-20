from django.db import models

# Create your models here.
# from __future__ import unicode_literals


class Nome(models.Model):
    NomeCompleto = models.CharField('Nome Completo', max_length=100)
    Endereco = models.CharField('Endereço', max_length=100)

# TITLE_CHOICES = (
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# )
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#     birth_date = models.DateField(blank=True, null=True)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name
#
# class Book(models.Model):
#     name = models.CharField(max_length=100)
#     authors = models.ManyToManyField(Author)
#
# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'title', 'birth_date']
#
# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']
