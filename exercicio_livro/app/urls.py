from django.contrib import admin
from django.urls import path, include
from livro.views import dados_livros, detalhe_livro, deletar_livros, atualizar_livro
urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', dados_livros, name='pagina-livro'),
    path('detalhe/<int:id>/', detalhe_livro, name='detalhe-livro'),
    path('deletar/<int:id>/', deletar_livros, name='deletar-livro'),
    path('atualizar/<int:id>/', atualizar_livro, name='atualiza-livro')
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('livro.urls')),

]