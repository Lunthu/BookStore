from django.contrib import admin
from blog.models import Items, Authors, Orders, Comments, Tags, Publishers
admin.site.register((Items, Authors, Orders, Comments, Tags, Publishers))
# Register your models here.