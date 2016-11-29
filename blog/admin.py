from django.contrib import admin
from blog.models import Items, Authors, Orders, Comments, Tags
admin.site.register((Items, Authors, Orders, Comments, Tags))
# Register your models here.