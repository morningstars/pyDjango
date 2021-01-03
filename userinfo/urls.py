from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^register', views.register),
    url(r'^logout', views.logout),
    url(r'^$', views.homepage),
    url(r'^test_form', views.test_form),
]
