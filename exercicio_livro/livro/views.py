from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
# Create your views here.
def dados_livros(request):
    livro = Livro.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        data_publicacao = request.POST.get('data_publicacao')
        descricao = request.POST.get('descricao')
        try:
            Livro.objects.create(titulo=titulo, autor=autor, data_publicacao=data_publicacao, descricao=descricao)
        except:
            return redirect('erro')
    return render(request, 'pagina_livro.html', {'livro': livro})

def detalhe_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    return render(request, 'pagina_detalhe.html', {'livro': livro})

def deletar_livros(request, id):
    curso = get_object_or_404(Livro, id=id)
    curso.delete()
    return redirect("pagina-livro")

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        data_publicacao = request.POST.get("data_publicacao")
        descricao = request.POST.get('descricao')
        
        if len(titulo) > 0:
            livro.titulo = titulo

        if len(autor) > 0:
            livro.autor = autor

        if len(data_publicacao) > 0:
            livro.data_publicacao = data_publicacao
        
        if len(descricao) > 0:
            livro.descricao = descricao

        livro.save()

        return redirect("pagina-livro")

    return render(request, 'atualizar_livro.html', {'livro': livro})

def erro(request):
    return render(request, 'pagina_erro.html')