from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def homepage(request):
    return HttpResponse("bookstore的首页")


def add(request):
    if request.method == 'GET':

        # title = request.GET.get('title', '')
        # price = request.GET.get('price', '')
        # pub = request.GET.get('pub', '')
        #
        # book = models.Book(title=title,
        #                    price=price,
        #                    pub=pub)
        # book.save()
        # return HttpResponse("get添加成功")

        return render(request, 'book_add.html')

    elif request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title', '')
        price = request.POST.get('price', '')
        pub = request.POST.get('pub', '')
        pub_date = request.POST.get('pub_date','')

        book = models.Book(title=title,
                           price=price,
                           pub=pub,
                           pub_date=pub_date)
        book.save()
        return HttpResponse("post添加成功")
