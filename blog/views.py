from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Orders, Items
from django.contrib.auth.models import User


class MainPage(TemplateView):
    template_name = 'First.html'


class OrdersView(TemplateView):
    template_name = 'Orders.html'
    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)
        j = list(Orders.objects.all())
        context['orders'] = j
        return context


class UserList(TemplateView):
    template_name = 'Userlist.html'

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        j = User.objects.all()
        context['userlist'] = j
        return context

class ItemList(TemplateView):
    template_name = 'Itemlist.html'

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        j = Items.objects.all()
        #j = users.objects.filter(id=kwargs['user_id'])
        context['itemlist'] = j
        return context

class ItemView(TemplateView):
    template_name = 'Items.html'
    model = Items

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        j = Items.objects.get(id=kwargs['item_id'])
        #j = users.objects.filter(id=kwargs['user_id'])
        context['items'] = j
        return context


class UserView(TemplateView):
    template_name = 'Users.html'
    model = User

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        j = User.objects.get(id=kwargs['user_id'])
        #j = users.objects.filter(id=kwargs['user_id'])
        context['users'] = j
        return context

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from blog.models import RegistrationForm


class RegisterFormView(FormView):
    form_class = RegistrationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
       # Создаём пользователя, если данные в форму были введены корректно.
       form.save()

       # Вызываем метод базового класса
       return super(RegisterFormView, self).form_valid(form)


from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")



