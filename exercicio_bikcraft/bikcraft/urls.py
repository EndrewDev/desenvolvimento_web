from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pagina-inicial'),
    path('sobre/', views.sobre, name='pagina-sobre'),
    path('cadastra_produtos/', views.cadastra_produtos, name='pagina-cadastraprodutos'),
    path('produtos/', views.produtos, name='pagina-produtos'),
    path('contados/', views.contados, name='pagina-contados'),
    path('cadastra_lojas/', views.cadastra_loja, name='cadastra-loja'),
    path('lojas/', views.lojas, name='pagina-loja'),
    path('pessoas/', views.pessoas, name='pagina-pessoas'),
    path('informacao_pessoas/', views.informacao_pessoas, name='pagina-informacaopessoas'),
    path('detalhe_bike/', views.detalhes_bikes, name='pagina-detalhebikes'),
    path('atualiza_lojas/<int:id>/', views.atualizado_lojas, name='atualiza-lojas'),
    path('adicionado/', views.adicionado, name='pagina-adicionado'),
    path('enviado/', views.enviado, name='pagina-enviado'),
    path('atualiza/<int:id>/', views.atualizado, name='pagina-atualizado'),
    path('atualiza_pessoas/<int:id>/', views.atualiza_pessoas, name='pessoas-atualiza'),
    path('atualiza_detalhe/<int:id>/', views.atualiza_detalhe, name='detalhe-atualiza'),
    path('atualizadosucesso/', views.atualizado_sucesso, name='pagina-atualizadosucesso'),
    path('deleta/<int:id>/', views.deleta, name='pagina-deleta'),
    path('deleta_lojas/<int:id>/', views.deleta_lojas, name='deleta-lojas'),
    path('deleta_pessoas/<int:id>/', views.deleta_pessoas, name='deleta-pessoas'),
    path('deleta_detalhe/<int:id>/', views.deleta_detalhe, name='detalhe-detela'),
    path('deletasucesso/', views.deleta_sucesso, name='pagina-deletasucesso'),
    path('deleta_lojas/<int:id>/', views.deleta_lojas, name='pagina_deletalojas'),
    path('erro/', views.erro, name='pagina-erro'),
]