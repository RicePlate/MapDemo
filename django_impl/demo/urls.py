from django.conf.urls import url

from demo.forms import AuthForm
from . import views
from django.contrib.auth import views as auth_views


app_name = 'demo'
urlpatterns = [
  url(r'^login/$', auth_views.login, kwargs={"authentication_form":AuthForm}, name='login'),
  url(r'^logout/$', auth_views.logout, {'next_page': '/demo/login'}, name='logout'),
  url(r'^signup/$', views.signup, name='signup'),
  url(r'^add/$', views.IndexView.as_view(), name='add'),
  url(r'^edit/(?P<mapid>[0-9]+)/$', views.IndexView.as_view(),name='edit'),
  url(r'^delete/(?P<mapid>[0-9]+)/$', views.IndexView.as_view(),name='delete'),
  url(r'^$', views.IndexView.as_view(), name='index'),
]