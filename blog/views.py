from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, DetailView, UpdateView
from django.views.generic.base import View
from blog.models import Orders, Items, Comments, Publishers, Authors, Tags
from blog.forms import RegistrationForm, CommentForm, OrderForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth import logout, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import AuthenticationForm
import random


class MainPage(TemplateView):
    template_name = 'First.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        item_list = Items.objects.get(id=random.randint(1,len(list(Items.objects.all()))))
        context['randombook'] = item_list
        topbooks = Items.objects.filter(item_publisher__id=1)[:5]
        context['topbooks'] = topbooks
        return context


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
        context['authors'] = Authors.objects.all()
        context['publishers'] = Publishers.objects.all()
        context['tags'] = Tags.objects.all()
        return context


def item_view(request, **kwargs):
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        Comments.objects.create(user_id=request.user, item_id=Items.objects.get(id=kwargs['item_id']), **form.cleaned_data)

    object = Items.objects.get(id=kwargs['item_id'])
    comment_list = Comments.objects.filter(item_id=kwargs['item_id']).order_by('-comment_date')
    paginator = Paginator(comment_list, 5)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, 'Items.html', {'comments': comments, 'item': object, 'form': form})


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
        context['users'] = j
        return context


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
       form.save()
       return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class OrderListView(TemplateView):
    template_name = 'Orders.html'
    model = Orders

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        j = Orders.objects.filter(user_id=self.request.user)
        context['orders'] = j
        return context	


class OrderCreate(CreateView):

    form_class = OrderForm
    success_url = '/orders/'
    template_name = 'order_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Items.objects.get(id=self.kwargs['item_id'])
        return context

    def form_valid(self, form):
        Orders.objects.create(user_id=self.request.user, order_status='p', item_id=Items.objects.get(id=self.kwargs['item_id']), **form.cleaned_data)
        return redirect('/orders/')


class OrderDetailsView(DetailView):
    model = Orders
    template_name = 'order_details.html'


class ItemAuthorList(TemplateView):
    template_name = 'authors_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemAuthorList, self).get_context_data(**kwargs)
        j = Items.objects.filter(author_id__id=kwargs['author_id'])
        paginator = Paginator(j, 3)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context['itemlist'] = items
        context['authors'] = Authors.objects.all()
        context['publishers'] = Publishers.objects.all()
        context['tags'] = Tags.objects.all()
        return context


class ItemPublisherList(TemplateView):
    template_name = 'authors_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemPublisherList, self).get_context_data(**kwargs)
        j = Items.objects.filter(item_publisher__id=kwargs['publisher_id'])
        paginator = Paginator(j, 3)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context['itemlist'] = items
        context['authors'] = Authors.objects.all()
        context['publishers'] = Publishers.objects.all()
        context['tags'] = Tags.objects.all()
        return context


class ItemTagsList(TemplateView):
    template_name = 'authors_list.html'

    def get_context_data(self, **kwargs):
        context = super(ItemTagsList, self).get_context_data(**kwargs)
        j = Items.objects.filter(item_genre__id=kwargs['tag_id'])
        paginator = Paginator(j, 3)
        page = self.request.GET.get('page')
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)

        context['itemlist'] = items
        context['authors'] = Authors.objects.all()
        context['publishers'] = Publishers.objects.all()
        context['tags'] = Tags.objects.all()
        return context