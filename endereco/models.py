from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField(max_length = 150)
    linha2 = models.CharField(max_length = 150, null = True, blank = True)
    cidade = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 70)
    pais = models.CharField(max_length = 70)

    def __str__(self):
        return self.linha1