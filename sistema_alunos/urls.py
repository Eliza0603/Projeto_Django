from django.contrib import admin
from django.urls import path, include


urlpatterns = [
path('admin/', admin.site.urls),
path('', include('alunos.urls')),
]






### alunos/apps.py



from django.apps import AppConfig




class AlunosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alunos'



