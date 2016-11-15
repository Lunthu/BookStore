from django.contrib import admin
from blog.models import Users, Items, Authors, Orders, Comments
admin.site.register((Users, Items, Authors, Orders, Comments,))
# Register your models here.