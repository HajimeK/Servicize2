from django.conf.urls import patterns, url

from translate import views

urlpatterns = patterns('',
  url(r'^$', views.home)
)
