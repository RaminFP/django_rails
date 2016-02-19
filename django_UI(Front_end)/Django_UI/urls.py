"""Django_UI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from App.Controller.User_Controller import search ,show,delete , index , create , edit
from App.View.User_View import User_View

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^',index),
    url(r'^$', User_View().User_Show, name='index'),
    url(r'^selectall', show),
    url(r'^searchname/$', search),
    url(r'^create/$', create),
    url(r'^delete/(?P<id>\w+)$', delete),
    url(r'^edit/(?P<id>\w+)$', edit ),



]
