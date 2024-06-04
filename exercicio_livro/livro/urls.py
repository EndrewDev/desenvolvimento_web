from django.urls import path
from livro.views import dados_livros, detalhe_livro, deletar_livros, atualizar_livro, erro
urlpatterns = [
    path('', dados_livros, name='pagina-livro'),
    path('detalhe/<int:id>/', detalhe_livro, name='detalhe-livro'),
    path('deletar/<int:id>/', deletar_livros, name='deletar-livro'),
    path('atualizar/<int:id>/', atualizar_livro, name='atualiza-livro'),
    path('erro/', erro, name='erro'),
]