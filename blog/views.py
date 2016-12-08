from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.views.generic.base import View
from blog.models import Orders, Items
from blog.forms import RegistrationForm, BookForm, OrderForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


class MainPage(TemplateView):
    template_name = 'First.html'

class UserList(FormView):
    template_name = 'Userlist.html'

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        j = User.objects.all()
        context['userlist'] = j
        return context

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ItemList(TemplateView):
    template_name = 'Itemlist.html'

    def get_context_data(self, **kwargs):
        context = super(ItemList, self).get_context_data(**kwargs)
        j = Items.objects.all()
        paginator = Paginator(j, 3)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context['itemlist'] = items
        return context

class ItemView(TemplateView):
    template_name = 'Items.html'

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        j = Items.objects.get(id = kwargs['item_id'])
        #j = users.objects.filter(id=kwargs['user_id'])
        context['item'] = j
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



#class OrdersView(TemplateView):
#    template_name = 'Orders.html'
#    model = Orders
#
#    def get(self, request):
#        def get_context_data(self, **kwargs):
#            context = super(OrdersView, self).get_context_data(**kwargs)
#            try:
#                j = Orders.objects.get(user_id=request.user.id)
#                #j = users.objects.filter(id=kwargs['user_id'])
#                context['orders'] = j
#            except ObjectDoesNotExist:
#                context['orders'] = 'У вас нет заказов'
#            return context


class OrderListView(TemplateView):
    template_name = 'Orders.html'
    model = Orders

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        j = Orders.objects.filter(user_id=self.request.user)
        #j = users.objects.filter(id=kwargs['user_id'])
        context['orders'] = j
        return context	


class OrderCreate(CreateView):
    form_class = OrderForm
    success_url = '/orders/'
    template_name = 'order_create.html'

    def form_valid(self, form):
        Orders.objects.create(user_id=self.request.user, order_status = 'p', item_id = Items.objects.get(id=1), **form.cleaned_data)
        return redirect('/orders/')


class OrderDetailsView(DetailView):
    model = Orders
    template_name = 'order_details.html'

#@login_required
#def ordercreate(request):
#    form = OrderForm
#    if request.method == "POST":
#        if form.is_valid():
#            Orders.objects.create(user_id=request.user.id, order_status = 'p', **form.cleaned_data)
#            return HttpResponseRedirect('/orders/')
#    else:
#        pass
#    return render(request, 'order_create.html', {'form': form})
