from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^add', views.add),
    url(r'^list', views.list_books),
    url(r'^filter/(\w+)', views.filter_books),
    url(r'^del/(\d+)', views.del_books),
    url(r'^mod/(\d+)', views.mod_books, name='mod'),
    url(r'^book', views.book_page, name='book')
]
