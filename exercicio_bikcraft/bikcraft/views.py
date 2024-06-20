from django.shortcuts import render, redirect, get_object_or_404
from .forms import BikeModelForm, ContadosModelForm, LojasModelForm, PessoasModelForm, DetalheModeForm
from .models import Bike, Contados, Lojas, Pessoas, DetalheBikes

def home(request):
    return render(request, 'bike.html')

def sobre(request):
    return render(request, 'sobre.html')

def cadastra_produtos(request):
    if request.method == 'POST':
        bike_form = BikeModelForm(request.POST, request.FILES)
        if bike_form.is_valid():
            bike_form.save()
            return redirect('pagina-adicionado')
    else:
        bike_form = BikeModelForm()
    return render(request, 'cadastra_produtos.html', {'form': bike_form})

def produtos(request):
    bike = Bike.objects.all()
    return render(request, 'produtos.html', {'produtos': bike})

def contados(request):
    if request.method == "POST":
        contados_form = ContadosModelForm(request.POST, request.FILES)
        if contados_form.is_valid():
            contados_form.save()
            return redirect('pagina-enviado')
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

def cadastra_loja(request):
    if request.method == 'POST':
        lojas_form = LojasModelForm(request.POST, request.FILES)
        if lojas_form.is_valid():
            lojas_form.save()
            return redirect('pagina-adicionado')
    else:
        lojas_form = LojasModelForm()
    return render(request, 'cadastra_lojas.html', {'lojas_form': lojas_form})

def lojas(request):
    lojas = Lojas.objects.all()
    return render(request, 'lojas.html', {'lojas': lojas})

def atualizado_lojas(request, id):
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

def deleta_lojas(request, id):
    deleta_lojas = get_object_or_404(Lojas, id=id)
    deleta_lojas.delete()
    return redirect('pagina-deletasucesso')

def pessoas(request):
    if request.method == 'POST':
        pessoas = PessoasModelForm(request.POST, request.FILES)
        if pessoas.is_valid():
            pessoas.save()
            return redirect('pagina-adicionado')
    else:
        pessoas = PessoasModelForm()
    return render(request, 'pessoas.html', {'pessoas': pessoas})
    
def informacao_pessoas(request):
    informacao_pessoas = Pessoas.objects.all()
    return render(request, 'informacao_pessoas.html', {'iformacao_pessoas': informacao_pessoas})

def atualiza_pessoas(request, id):
    pessoas_atualiza = get_object_or_404(Pessoas, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        opcao_lojas = request.POST.get('opcao_lojas')

        if len(nome) > 0:
            pessoas_atualiza.nome = nome
        if len(cpf) > 0:
            pessoas_atualiza.cpf = cpf
        if len(opcao_lojas) > 0:
            pessoas_atualiza.opcao_lojas = opcao_lojas
        pessoas_atualiza.save()
    return redirect('pagina-atualizadosucesso')
    
def deleta_pessoas(request, id):
    pessoas = get_object_or_404(Pessoas, id=id)
    pessoas.delete()
    return redirect('pagian-deletasucesso')

def detalhes_bikes(request):
    if request.method == 'POST':
        detalhe_bike = DetalheModeForm(request.POST, request.FILES)
        if detalhe_bike.is_valid():
            detalhe_bike.save()
            return redirect('pagina-adicionado')
    else:
        detalhe_bike = DetalheModeForm()
    return render(request, 'detalhe_bike.html', {'detalhe': detalhe_bike})

def detalhe(request):
    detalhe = DetalheBikes.objects.all()
    return render(request, 'pagina-detalhemais', {'detalhe': detalhe})

def atualiza_detalhe(request, id):
    detalhe_atualiza = get_object_or_404(DetalheBikes, id=id)
    if request.method == 'POST':
        opcao = request.POST.get('opcao')
        detalhe = request.POST.get('detalhe')

        if len(opcao) > 0:
            detalhe_atualiza.opcao = opcao
        if len(detalhe) > 0:
            detalhe_atualiza.detalhe = detalhe
        detalhe_atualiza.save()
    return redirect('pagina-atualizadosucesso')

def deleta_detalhe(request, id):
    detalhe_deleta = get_object_or_404(DetalheBikes, id=id)
    detalhe_deleta.delete()
    return redirect('pagina-deletasucesso')