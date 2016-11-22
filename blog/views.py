from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Users, Orders, Items


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
        j = Users.objects.all()
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
    model = Users

    def dispatch(self, request, *args, **kwargs):
        print(request)
        print(kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        j = Users.objects.get(id=kwargs['user_id'])
        #j = users.objects.filter(id=kwargs['user_id'])
        context['users'] = j
        return context


# Create your views here.
