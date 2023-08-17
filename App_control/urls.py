from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views
from App_control.views import (
  PublicacionLista, PublicacionDetalle, PublicacionUpdate, PublicacionDelete, PublicacionCreacion, ComentarioPagina, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView,
)

urlpatterns = [

    
 
    path('', HomeView.as_view(), name='base'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='App_control/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/', views.password_exitoso, name='password_exitoso'),
    path('acercaDeMi/', views.about, name='about'),

    path('PublicacionCreacion/', PublicacionCreacion.as_view(), name='CrearPost'),
    path('PublicacionLista/', PublicacionLista.as_view(), name='ListaPost'),
    path('PublicacionDetalle/', PublicacionDetalle.as_view(), name='DetallePost'),
    path('PublicacionUpdate/', PublicacionUpdate.as_view(), name='UpdatePost'),
    path('PublicacionDelete/', PublicacionDelete.as_view(), name='DeletePost'),
    path('ComentarioPagina/', ComentarioPagina.as_view(), name='ComentarPost'),

 
]

