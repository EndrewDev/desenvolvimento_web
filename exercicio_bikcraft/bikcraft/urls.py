from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pagina-inicial'),
    path('sobre/', views.sobre, name='pagina-sobre'),
    path('produtos/', views.produtos, name='pagina-produtos'),
    path('lojas/', views.lojas, name='pagina-lojas'),
    path('contados', views.contados, name='pagina-contados'),
    path('adicionado/', views.adicionado, name='pagina-adicionado'),
    path('enviado/', views.enviado, name='pagina-enviado'),
    path('atualiza/<int:id>/', views.atualizado, name='pagina-atualizado'),
    path('atualizadosucesso/', views.atualizado_sucesso, name='pagina-atualizadosucesso'),
    path('deleta/<int:id>/', views.deleta, name='pagina-deleta'),
    path('deletasucesso/', views.deleta_sucesso, name='pagina-deletasucesso'),
    path('erro/', views.erro, name='pagina-erro'),
]