from django.urls import path, include
from rest_framework import routers
from .views import AlunoViewSet, DisciplinaViewSet, NotaViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = 'alunos'

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='aluno')
router.register(r'disciplinas', DisciplinaViewSet, basename='disciplina')
router.register(r'notas', NotaViewSet, basename='nota')

urlpatterns = [
    path('', views.home, name='home'),
    path('alunos/', views.aluno_list, name='aluno_list'),
    path('alunos/novo/', views.aluno_create, name='aluno_create'),
    path('notas/lancar/', views.lancar_nota, name='lancar_nota'),
    path('alunos/<int:aluno_id>/boletim/', views.boletim, name='boletim'),

    #API
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),

]

