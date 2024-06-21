from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina-inicial')
        else:
            return redirect('pagina-erro')
    form = UserCreationForm()
    return render(request, 'cadastra_usuario.html', {'form': form})

def acessar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('pagina-inicial')
        else:
            return redirect('erro-acessa')
    form = AuthenticationForm()
    return render(request, 'acessa.html', {'form': form})

def sair(request):
    logout(request)
    return redirect('pagina-inicial')