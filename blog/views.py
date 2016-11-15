from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Users

class MyFirst(TemplateView):
    template_name = 'First.html'
    def get_context_data(self, **kwargs):
        context = super(MyFirst, self).get_context_data(**kwargs)
        i = list(Users.objects.all())
        context['userlist'] = i
        return context
# Create your views here.
