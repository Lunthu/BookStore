from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Users

class MyFirst(TemplateView):
    template_name = 'First.html'
    def get_context_data(self, **kwargs):
        context = super(MyFirst, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all()
        return context
# Create your views here.
