from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list      import ListView
from django.views.generic.edit      import DeleteView, UpdateView, CreateView
from django.views.generic.detail    import DetailView


from .models import User

# Create your views here.


class UserBaseView(View):
    template_name = 'user.html'
    model = User
    fields = '__all__'
    success_url = reverse_lazy('users:all')
    extra_context = {"hide_main": True}  # se añade 'hide_main' al extra_context

class UsersListView(UserBaseView,ListView):
    template_name = "user.html"
    
class UsersDetailView(UserBaseView,DetailView):
    template_name = "user_detail.html"

class UsersCreateView(UserBaseView,CreateView):
    template_name = "user_create.html"
    extra_context = {
        "tipo": "Crear user",
        "hide_main": True
    }

class UsersUpdateView(UserBaseView,UpdateView):
    template_name = "user_create.html"
    extra_context = {
        "hide_main": True,
        "tipo": "Actualizar user"
    }

class UsersDeleteView(UserBaseView,DeleteView):
    template_name = "user_delete.html"
    extra_context = {
        "hide_main": True,
        "tipo": "Borrar user"
    }



# urls.py ----->>>>