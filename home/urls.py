from django.conf.urls import url
from . import views
app_name ='home'

urlpatterns = [
    url(r'^$', views.home, name='base'),
    url(r'^home/$', views.home, name='base'),
    url(r'^base/$', views.home, name='base'),
   #url(r'^home/$', include('omk.urls')),
    url(r'^about/$', views.about, name='about'),
    url(r'^mentor/$', views.mentor, name='mentor'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^index/$', views.index, name='index'),

    ]