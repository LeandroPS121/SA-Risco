from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.data}"
