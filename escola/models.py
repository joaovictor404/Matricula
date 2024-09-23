from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=300)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

