from django import forms
from . models import Nome

# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(
#         max_length=3,
#         widget=forms.Select(choices=TITLE_CHOICES),
#     )
#     birth_date = forms.DateField(required=False)
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

class NomeForm(forms.ModelForm):
    #nome = forms.CharField(max_length=100)
    class Meta:
        model = Nome
        fields = ['NomeCompleto', 'Endereco']
