from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.

def homepage(request):
    return render(request, 'book_homepage.html')


def list_books(request):
    # 从模型中取数据
    books = models.Book.objects.all()

    # 排序
    # books = models.Book.objects.order_by('-price')

    # 渲染模板
    return render(request, 'book_list.html', locals())


def filter_books(request, pub):
    # 筛选
    books = models.Book.objects.filter(pub=pub)
    return render(request, 'book_list.html', locals())


def add(request):
    if request.method == 'GET':
        return render(request, 'book_add.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        price = request.POST.get('price', '')
        pub = request.POST.get('pub', '')
        pub_date = request.POST.get('pub_date', '')

        # 方法一
        # book = models.Book.objects.create(
        #     title=title, price=price, pub=pub
        # )

        # 方法二
        book = models.Book(title=title,
                           price=price,
                           pub=pub,
                           pub_date=pub_date)
        book.save()
        return HttpResponse("post添加成功")


def del_books(request, book_id):
    try:
        book = models.Book.objects.get(id=book_id)
        book.delete()
        return HttpResponseRedirect("/book/list")
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息")


def mod_books(request, book_id):
    try:
        book = models.Book.objects.get(id=book_id)
    except:
        return HttpResponse("没有找到ID为" + book_id + "的图书信息")

    if request.method == 'GET':
        # get时需要传参
        print(locals())
        return render(request, 'book_mod.html', locals())
    else:
        try:
            price = request.POST.get('price', '0.00')
            book.price = price
            book.save()
            return HttpResponse('修改成功')
        except:
            return HttpResponse('修改失败')
