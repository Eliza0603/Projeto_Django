from rest_framework import serializers
from .models import Aluno, Disciplina, Nota
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('id','username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    class AlunoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Aluno
            fields = '__all__'

    class NotaSerializer(serializers.ModelSerializer):
        aluno = AlunoSerializer(read_only=True)
        aluno_id = serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all(), source='aluno', write_only=True)
        disciplina = DisciplinaSerializer(read_only=True)
        disciplina_id = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all(), source='disciplina', write_only=True)

        class Meta:
            model = Nota
            fields = ('id','aluno','aluno_id','disciplina','disciplina_id','valor','data','lancado_por')
            read_only_fields = ('data','lancado_por')
