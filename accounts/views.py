from django.shortcuts import render
from django.views.generic import CreateView,FormView,UpdateView
from .forms import UserRegisterForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login

# Create your views here.


class RegisterView(FormView):
    template_name='accounts/register.html'
    form_class=UserRegisterForm
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        user=form.save()
        login(self.request, user)
        
        return super().form_valid(form)

class ChangeUserForm(UpdateView):
    template_name='accouts/user_change.html'
    form_class=UserUpdateForm
    success_url=reverse_lazy('home')
    
    def get_object(self):
        return self.request.user


class UserLoginView(LoginView):
    template_name='accounts/Login.html'
    next_page='home'