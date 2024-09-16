from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno

def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'index.html', {'alunos': alunos})
# Create your views here.
