from django.shortcuts import render, redirect, get_object_or_404
from .models import Bike, Contados
from .forms import bikeform

def home(request):
    return render(request, 'bike.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    if request.method == 'POST':
        bike_form = bikeform(request.POST, request.FILES)
        if bike_form.is_valid():
            bike_form.save()
            return redirect('pagina-adicionado')
        else:
            bike_form = bikeform()
    return render(request, 'produtos.html', {'bikes': bike_form})

def lojas(request):
    bike = Bike.objects.all()
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        foto = request.POST.get('foto')
        try:
            
    return render(request, 'lojas.html')

def contados(request):
    contado = Contados.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        try:
            Contados.objects.create(nome=nome, email=email, mensagem=mensagem)
        except:
            return redirect('erro')
    return render(request, 'contados.html', {'contados': contado})

def adicionado(request):
    return render(request, 'adicionado.html')

def enviado(request):
    return render(request, 'enviado.html')