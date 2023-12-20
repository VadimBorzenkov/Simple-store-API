from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


from users.forms import UserLoginForm
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    title = 'Store - Авторизация'
    template_name = 'users/base.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')


class UserLogoutView(TitleMixin, LogoutView):
    title = 'Store - Выход'

    def dispatch(self, request, *args, **kwargs):
        # Вызываем метод dispatch из базового класса
        response = super().dispatch(request, *args, **kwargs)

        return redirect('index')
