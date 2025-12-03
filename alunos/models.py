from django.db import models
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=30, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

    class Disciplina(models.Model):
        nome = models.CharField(max_length=150, unique=True)

        def __str__(self):
            return self.nome

    class Nota(models.Model):
        aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
        disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
        valor = models.DecimalField(max_digits=5, decimal_places=2)
        data = models.DateField(auto_now_add=True)
        lancado_por = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('aluno', 'disciplina')

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}: {self.valor}"