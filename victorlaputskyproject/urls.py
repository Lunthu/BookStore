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
from blog.views import OrderView, UserView, MainPage, UserList, ItemView, ItemList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainPage.as_view(), name='main'),
    url(r'^orders/$', OrderView.as_view(), name='orders'),
	url(r'^orders/create/$', views.OrderCreate.as_view(), name='create_order'),
    url(r'^userlist/$', UserList.as_view(), name='users'),
    url(r'^itemlist/$', ItemList.as_view(), name='items'),
    url(r'^item/(?P<item_id>[0-9]+)/$', ItemView.as_view(), name='item'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^user/(?P<user_id>[0-9]+)/$', UserView.as_view(), name = 'user')

]
