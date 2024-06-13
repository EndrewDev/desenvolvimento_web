from django import forms
from .models import Bike, Contados

class BikeModelForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

    def clean_preco(self):
        preco_cadastra = self.cleaned_data.get('preco')
        if preco_cadastra < 200:
            self.add_error('preco', 'O preço não pode ser menor do que R$200')
        return preco_cadastra
    
    def clean_foto(self):
        tamanho_maximo = 2
        imagem = self.cleaned_data.get('foto')
        tamanho_imagem = tamanho_maximo * 1024 * 1024
        if imagem.size > tamanho_imagem:
            raise forms.ValidationError('A imagem tem um tamanho maior que o suportado')
        return imagem

class ContadosModelForm(forms.ModelForm):
    class Meta:
        model = Contados
        fields = '__all__'

    def clean_email(self):
        email_verificado = self.cleaned_data.get('email')
        def verificar_email_gmail(email):
            return email.endswith('@gmail.com')
        lista_email = []
        lista_email.append(email_verificado)
        for email in lista_email:
            if verificar_email_gmail(email):
                self.add_error('email', 'E-mail errado')
        return email