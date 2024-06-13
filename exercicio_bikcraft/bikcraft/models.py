from django.db import models

class Bike(models.Model):
    modelo = models.CharField(max_length=255, verbose_name='Modelo')
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    foto = models.ImageField(upload_to='bikcraft/', blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return self.modelo
    
class Contados(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    email = models.CharField(max_length=255, verbose_name='E-mail')
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.email
    
class Lojas(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    produtos = models.ManyToManyField(Bike, verbose_name='Produtos')
    cnpj = models.CharField(max_length=25, verbose_name='CNPJ')
    detalhe = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.nome