from django import forms
from .models import Bike, Contados

""" class bikeform(forms.Form):
    modelo = forms.CharField(max_length=255)
    preco = forms.FloatField()
    descricao = forms.CharField(widget=forms.Textarea)
    foto = forms.ImageField()

    def save(self):
        bike = Bike(
            modelo = self.cleaned_data['modelo'],
            preco = self.cleaned_data['preco'],
            descricao = self.cleaned_data['descricao'],
            foto = self.cleaned_data['foto'],
            )
        bike.save()
        return bike """

class BikeModelForm(forms.ModelForm):
    class meta:
        model = Bike
        fields = '__all__'

    def clean_preco(self):
        preco_cadastra = self.cleaned_data['preco']
        if preco_cadastra < 200:
            self.add_error('preco', 'O preço não pode ser menor do que R$200')
        return preco_cadastra
    
    def clean_foto(self):
        tamanho_maximo = 2
        imagem = self.cleaned_data.get('foto')
        tamanho_imagem = tamanho_maximo * 1024 * 1024
        if imagem.size > tamanho_imagem:
            return forms.ValidationError('A imagem tem um tamanho maior que o suportado')
        return imagem
    
class ContadosModelForm(forms.ModelForm):
    class meta:
        model = Contados
        fields = '__all__'

    def clean_email(self):
        e_mail = self.cleaned_data['email']
        if len(e_mail) != 'gmail':
            self.add_error('email', 'E-mail errado')
        return e_mail