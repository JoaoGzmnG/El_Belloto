from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('form_pendientes', views.pendientes, name='pendientes'),
    path('form_empresas', views.empresas, name='empresas'),
    path('sobre_mi', views.sobre_mi, name='sobre_mi'),
    path('form_pendientes', views.pendientes_post, name='pendientes_post')
]

