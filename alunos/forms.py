from django import forms
from .models import Aluno, Nota

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','matricula','data_nascimento']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['aluno','disciplina','valor']