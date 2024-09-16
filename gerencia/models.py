from django.db import models

class Aluno (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    imagem = models.ImageField(upload_to='imagem', null=True, blank=True)
    def __str__(self):
        return self.nome