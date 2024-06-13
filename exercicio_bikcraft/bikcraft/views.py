from django.shortcuts import render, redirect, get_object_or_404
from .forms import BikeModelForm, ContadosModelForm
from .models import Bike, Contados

def home(request):
    return render(request, 'bike.html')

def sobre(request):
    return render(request, 'sobre.html')

def produtos(request):
    if request.method == 'POST':
        bike_form = BikeModelForm(request.POST, request.FILES)
        if bike_form.is_valid():
            bike_form.save()
            return redirect('pagina-adicionado')
        else:
            return redirect('pagina-erro')
    else:
        bike_form = BikeModelForm()
    return render(request, 'produtos.html', {'form': bike_form})

def lojas(request):
    bike = Bike.objects.all()
    return render(request, 'lojas.html', {'loja': bike})

def contados(request):
    if request.method == "POST":
        contados_form = ContadosModelForm(request.POST, request.FILES)
        if contados_form.is_valid():
            contados_form.save()
            return redirect('pagina-enviado')
        else:
            return redirect('pagina-erro')
    else:
        contados_form = ContadosModelForm()
    return render(request, 'contados.html', {'contados': contados_form})

def adicionado(request):
    return render(request, 'adicionado.html')

def enviado(request):
    contados = Contados.objects.all()
    return render(request, 'enviado.html', {'contados': contados})

def atualizado(request, id):
    bike = get_object_or_404(Bike, id=id)

    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        foto = request.POST.get('foto')

        if len(modelo) > 0:
            bike.modelo = modelo
        if len(preco) > 0:
            bike.preco = preco
        if len(descricao) > 0:
            bike.descricao = descricao
        if len(foto) > 0:
            bike.foto = foto
        bike.save()
        return redirect('pagina-atualizadosucesso')
        
    return render(request, 'ataulizado.html', {'atualizado': bike})
def atualizado_sucesso(request):
    return render(request, 'atualizado_sucesso.html')

def deleta(request, id):
    bike = get_object_or_404(Bike, id=id)
    bike.delete()
    return redirect('pagina-deletasucesso')
def deleta_sucesso(request):
    return render(request, 'deleta_sucesso.html')

def erro(request):
    return render(request, 'erro.html')