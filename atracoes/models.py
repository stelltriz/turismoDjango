from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario = models.TextField()
    idademin = models.IntegerField()

    def __str__(self):
        return self.nome