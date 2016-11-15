from django.contrib import admin
from blog.models import Users, Items, Authors, Orders, Comments
admin.site.register(Users)
admin.site.register(Items)
admin.site.register(Authors)
admin.site.register(Orders)
admin.site.register(Comments)
# Register your models here.