from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno, Disciplina, Nota
from .forms import AlunoForm, NotaForm

# API imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import AlunoSerializer, DisciplinaSerializer, NotaSerializer, UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics

# Registro via API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

#API VIEWSETS
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by('-criado_em')
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all().order_by('nome')
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

class NotaViewSet(viewsets.ModelViewSet):
     queryset = Nota.objects.all().select_related('aluno','disciplina')
     serializer_class = NotaSerializer
     permission_classes = [IsAuthenticated]

     def perform_create(self, serializer):
         serializer.save(lancado_por=self.request.user)

# Web views (templates)
def home(request):
    return render(request, 'alunos/home.html')

@login_required
def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/aluno_list.html', {'alunos': alunos})

@login_required
def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos:aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'alunos/aluno_form.html', {'form': form})


@login_required
def lancar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            nota = form.save(commit=False)
            nota.lancado_por = request.user
            nota.save()
            return redirect('alunos:aluno_list')
    else:
        form = NotaForm()
    return render(request, 'alunos/lancar_nota.html', {'form': form})

@login_required
def boletim(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    notas = Nota.objects.filter(aluno=aluno).select_related('disciplina')
    valores = [float(n.valor) for n in notas]
    media = sum(valores)/len(valores) if valores else None
    return render(request, 'alunos/boletim.html', {'aluno': aluno, 'notas': notas, 'media': media})
