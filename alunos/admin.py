from django.contrib import admin
from .models import Aluno, Disciplina, Nota


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','matricula','data_nascimento','criado_em')
    search_fields = ('nome','matricula')

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'valor', 'data', 'lancado_por')
    list_filter = ('disciplina',)