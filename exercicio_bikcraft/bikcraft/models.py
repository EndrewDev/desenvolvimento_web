from django.db import models

class Bike(models.Model):
    modelo = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField()
    foto = models.ImageField(upload_to='bikcraft/', blank=True, null=True)

    def __str__(self):
        return self.modelo
    
class Contados(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome