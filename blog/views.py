from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views.generic.base import View
from blog.models import Orders, Items
from blog.forms import RegistrationForm, BookForm, CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

class MainPage(TemplateView):
    template_name = 'First.html'

class UserList(FormView):
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

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        j = Items.objects.get(id = kwargs['item_id'])
        #j = users.objects.filter(id=kwargs['user_id'])
        context['itemlist'] = j
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



class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
       form.save()
       return super(RegisterFormView, self).form_valid(form)


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")



class OrdersView(TemplateView):
    template_name = 'Orders.html'
    model = Orders

    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data(**kwargs)
        try:
            j = Orders.objects.get(user_id=1)
            #j = users.objects.filter(id=kwargs['user_id'])
            context['orders'] = j
        except Vehicle.vehicledevice.device.DoesNotExist:
            context['orders'] = 'У вас нет заказов'
        return context

