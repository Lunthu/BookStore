from django.contrib import admin
from blog.models import Users, Items, Authors, Orders, Comments, Tags
admin.site.register((Users, Items, Authors, Orders, Comments, Tags))
# Register your models here.