from django.shortcuts import render

def home(request):
    return render(request, 'bike.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    return render(request, 'produtos.html')

def lojas(request):
    return render(request, 'lojas.html')