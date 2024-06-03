from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pagina-inicial'),
    path('sobre/', views.sobre, name='pagina-sobre'),
    path('formulario', views.formulario, name='pagina-formulario'),
    path('produtos/', views.produtos, name='pagina-produtos'),
    path('lojas/', views.lojas, name='pagina-lojas')
]