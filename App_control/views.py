from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.db.models import Q



from App_control.models import Articulos, delivery, Cliente, Publicacion, Comentario
from App_control.forms import ArticuloFormulario, FormularioComentario, FormularioRegistroUsuario, FormularioEdicion, FormularioNuevoPublicacion, ActualizacionPublicacion, FormularioCambioPassword




class clienteCreateView(CreateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'email')
    success_url = reverse_lazy('lista_cliente')


class clienteDetailView(DetailView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')

 
class clienteUpdateView(UpdateView):
    model = Cliente
    fields = ('nombre', 'apellido', 'dni', 'email')
    success_url = reverse_lazy('lista_cliente')



class clienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('lista_cliente')

class deliveryListView(ListView):
    model = delivery
    template_name = 'App_control/lista_delivery.html'


class deliveryCreateView(CreateView):
    model = delivery
    fields = ('nombre', 'ubicacion', 'habilitado')
    success_url = reverse_lazy('lista_delivery')


class deliveryDetailView(DetailView):
    model = delivery
    success_url = reverse_lazy('lista_delivery')


class deliveryUpdateView(UpdateView):
    model = delivery
    fields = ('nombre', 'ubicacion', 'habilitado')
    success_url = reverse_lazy('lista_delivery')



class deliveryDeleteView(DeleteView):
    model = delivery
    success_url = reverse_lazy('lista_delivery')


########################################## NEW #####################

class PublicacionLista(LoginRequiredMixin, ListView):
    model = Publicacion
    template_name = 'App_control/ListaPublicacion.html'
    login_url = '/login/'

class PublicacionDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    success_url = reverse_lazy('DetallePost')
    template_name= 'App_control/PublicacionDetalle.html'

class PublicacionUpdate(LoginRequiredMixin, UpdateView):
    model = Publicacion
    fields = ('titulo', 'contenido', 'imagencontenido')
    success_url = reverse_lazy('UpdatePost')
    template_name= 'App_control/PublicacionUpdate.html'

class PublicacionDelete(LoginRequiredMixin, DeleteView):
    model = Publicacion
    success_url = reverse_lazy('ListaPost')
    template_name= 'App_control/PublicacionDelete.html'


class PublicacionCreacion(LoginRequiredMixin, CreateView):
    model = Publicacion
    form_class = FormularioNuevoPublicacion
    success_url = reverse_lazy('base')
    template_name = 'App_control/PublicacionCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PublicacionCreacion, self).form_valid(form)

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'App_control/base.html'

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'App_control/comentario.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

def about(request):
    return render(request, 'App_control/acercaDeMi.html', {})

class LoginPagina(LoginView):
    template_name = 'App_control/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('base')

    def get_success_url(self):
        return reverse_lazy('base')

class RegistroPagina(FormView):
    template_name = 'App_control/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('base')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'App_control/edicionPerfil.html'
    success_url = reverse_lazy('base')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'App_control/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'App_control/passwordExitoso.html', {})

def about(request):
    return render(request, 'App_control/acercaDeMi.html', {})

