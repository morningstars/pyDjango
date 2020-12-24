"""python_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^page1/$', views.page1),
    # url(r'^page2/$', views.page2),
    # url(r'^page3/$', views.hello),
    # url(r'^$', views.homepage),

    url(r'^year/(\d{4})$', views.page_year),
    url(r'^birthday/(\d{4})/(\d{1,2})/(\d{1,2})$', views.birthday),
    url(r'^birthday2$', views.birthday2),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person),
    url(r'^(\d+)/add/(\d+)', views.add),
    url(r'^(\d+)/sub/(\d+)', views.sub),
    url(r'^test$', views.test_request),
    url(r'^test2$', views.test_request2),
    url(r'^test_get$', views.test_get),
    url(r'^show_info', views.show_info),

    url(r'^shebao$', views.shebao),
    url(r'^shebao_result$', views.shebao_result),

    url(r'^page1', views.page1_templates, name='page1'),
    url(r'^page2', views.page2_render),
    url(r'^page3', views.page3),
    url(r'^page4', views.page4),

    url(r'^$', views.homepage, name='index'),
    url(r'^sport', views.sport_homepage),

    url(r'^pages', views.pages),
    url(r'^people/(\w+)', views.people, name='people'),
    url(r'^info/(\w+)', views.info, name='info')
]
