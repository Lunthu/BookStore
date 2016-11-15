from django.contrib import admin
from blog.models import Users, Items, Authors, Orders, ItemStatusList, OrderStatusList, Comments
admin.site.register(Users)
admin.site.register(Items)
admin.site.register(Authors)
admin.site.register(ItemStatusList)
admin.site.register(OrderStatusList)
admin.site.register(Orders)
admin.site.register(Comments)
# Register your models here.
