from django.shortcuts import render, redirect, render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from blog.models import Users, Orders, Items
from django.http import HttpResponse
import datetime

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
        context['item'] = j
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

def current_time(request):
    now = datetime.datetime.now()
    return now

def title(request, title):
    context = {}
    context['title'] = title
    html = "<html><body>My title is<br>%s<br><br></body></html>" % title
    return html

def simple(request):
    context = {}
    context['time'] = current_time(request)
    return render_to_response('First.html', context)

def simple2(request, id):
    object = get_object_or_404(Items, pk=id)
    return redirect(object)

def simple3(request):
    context = {}
    context['item'] = get_list_or_404(Items, id = 1)
    return render_to_response('Items.html', context)