from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='base'),
    url(r'^home/$', views.home, name='base'),
   #url(r'^home/$', include('omk.urls')),
    url(r'^About_Us/$', views.About_Us) ,


    ]
