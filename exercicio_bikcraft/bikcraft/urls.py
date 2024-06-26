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
    path('cadastra_pessoas/', views.cadastra_pessoas, name='cadastra-pessoas'),
    path('vendedores/', views.vendedores, name='pagina-vendedores'),
    path('detalhe_bike/', views.detalhes_bikes, name='pagina-detalhebikes'),
    path('atualiza_lojas/<int:id>/', views.atualizado_lojas, name='atualiza-lojas'),
    path('adicionado-produtos/', views.adicionado, name='pagina-adicionado-produto'),
    path('enviado/', views.enviado, name='pagina-enviado'),
    path('atualiza_produtos/<int:id>/', views.atualizado_produtos, name='pagina-atualizado'),
    path('atualiza_pessoas/<int:id>/', views.atualiza_pessoas, name='pessoas-atualiza'),
    path('atualiza_detalhe/<int:id>/', views.atualiza_detalhe, name='detalhe-atualiza'),
    path('atualizado_sucessoprodutos/', views.atualizado_sucessoprodutos, name='pagina-atualizadosucesso-produtos'),
    path('deleta_sucesso_produtos/', views.deleta_sucesso_produtos, name='deleta-sucesso-produtos'),
    path('deleta_produtos/<int:id>/', views.deleta_produtos, name='deleta-produtos'),
    path('deleta_lojas/<int:id>/', views.deleta_lojas, name='deleta-lojas'),
    path('deleta_pessoas/<int:id>/', views.deleta_pessoas, name='deleta-pessoas'),
    path('deleta_detalhe/<int:id>/', views.deleta_detalhe, name='detalhe-detela'),
    path('deleta_lojas/<int:id>/', views.deleta_lojas, name='pagina_deletalojas'),
    path('adicionado_lojas/', views.adicionado_lojas, name='adicionado-lojas'),
    path('atualizado-lojas/', views.atualizado_lojas, name='atualizado-lojas'),
    path('atualiza_sucessolojas/', views.atualiza_sucessolojas, name='atualiza-sucessolojas'),
    path('deleta_sucesso_lojas/', views.deleta_sucesso_lojas, name='deleta-sucesso-lojas'),
    path('adicionado_pessoas/', views.adicionado_pessoas, name='adicionado-pessoas'),
    path('atualizado_sucesso_pessoas/', views.atualizado_sucesso_pessoas, name='atualizado-sucesso-pessoas'),
    path('deleta_sucesso_pessoas/', views.deleta_sucesso_pessoas, name='deleta-sucesso-pessoas'),
    path('adicionado_detalhe/', views.adicionado_detalhe, name='adicionado-detalhe'),
    path('deleta_sucesso_detalhes/', views.deleta_sucesso_detalhes, name='deleta-sucesso-detalhes'),
    path('atualizado_sucesso_detalhe/', views.atualizado_sucesso_detalhe, name='atualizado-sucesso-detalhe'),
    path('detalhes/', views.detalhe, name='pagina-detalhe'),
    path('cadastra_detalhe/', views.detalhes_bikes, name='cadastra-detalhe'),
    path('adicionado_detalhe/', views.adicionado_detalhe, name='adicionado-detalhe'),
]