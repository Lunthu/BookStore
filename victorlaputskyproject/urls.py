"""victorlaputskyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import blog.views as views
from blog.views import OrdersView, UserView, MainPage, UserList, ItemView, ItemList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^orders/$', OrdersView.as_view(), name='orders'),
    url(r'^userlist/$', UserList.as_view(), name='users'),
    url(r'^itemlist/$', ItemList.as_view(), name='item'),
    url(r'^item/(?P<item_id>[0-9]+)/$', ItemView.as_view(), name='item'),
    url(r'^user/(?P<user_id>[0-9]+)/$', UserView.as_view(), name='user'),
    url(r'^title/(?P<title>[a-zA-Z0-9]+)/$', views.title, name='time'),
    url(r'^rrr-(?P<id>[0-9]+)$', views.simple2),
    url(r'^item/first_book$', views.simple3),
    url(r'^$', views.simple, name='main')


]
