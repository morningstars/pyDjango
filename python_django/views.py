from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.template import loader
from django.shortcuts import render
import os

# 导入当前项目配置文件的setting模块
# from . import settings
from django.conf import settings


def page1(request):
    print("page1被调用")
    return HttpResponse("这是page1页")


def page2(request):
    html = '''
    <html>
    <head><title>这是页面2</title></head>
    <body>
        <h1>这是H1</h1>
        <h2 style = "color:red;">这是H2</h2>
    </body>
    </html>
    '''
    return HttpResponse(html)


def hello(request):
    html = '<h1>hello world</h1>'
    return HttpResponse(html)


# def homepage(request):
#     html = "这是首页"
#     return HttpResponse(html)


# 带有参数的视图函数
def page_year(request, y):
    html = "参数是:" + y
    print(type(y))
    return HttpResponse(html)


# 带有多个参数的视图函数
def birthday(request, y, m, d):
    html = "生日：" + y + "年" + m + "月" + d + "日"
    return HttpResponse(html)


def birthday2(request):
    if request.method == 'GET':
        y = request.GET.get('year', '')
        m = request.GET.get('month', '')
        d = request.GET.get('day', '')
        html = "生日为：" + y + '年' + m + '月' + d + '日'
    return HttpResponse(html)


def person(request, name, age):
    html = "<h1> 姓名：" + name + "</h1>"
    html += "<h1> 年龄：" + age + "</h1>"
    return HttpResponse(html)


def add(request, a, b):
    html = str(int(a) + int(b))
    return HttpResponse(html)


def sub(request, a, b):
    html = str(int(a) - int(b))
    return HttpResponse(html)


def show_info(request):
    html = '<p>' + "请求方式:" + request.method + '</p>'

    html += '<p>' + "request.scheme:" + request.scheme + '</p>'
    html += '<p>' + "request.GET:" + str(request.GET) + '</p>'
    html += '<p>' + "request.POST:" + str(request.POST) + '</p>'
    html += '<p>' + "request.COOKIES:" + str(request.COOKIES) + '</p>'
    html += '<p>' + "request.scheme:" + request.scheme + '</p>'
    html += '<p>' + "request.META:" + str(request.META) + '</p>'
    html += '<p>' + "request.META['REMOTE_ADDR']:" + str(request.META['REMOTE_ADDR']) + '</p>'

    return HttpResponse(html)


def test_request(request):
    print("request path=", request.path)
    print("request method=", request.method)
    return HttpResponse("OK!")


def test_request2(request):
    # 重定向到
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect("https://www.jd.com")


def test_get(request):
    # a = request.GET['a']
    # c = request.GET.get('c', '没有值')
    # print("a = ", a)
    # print("c = ", c)
    for k in request.GET:
        print("键：", k, "值", request.GET[k])
    return HttpResponse("GET请求成功")


def search(request):
    html = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>搜索</title>
    </head>
    <body>
        <form method="post" action="/search">
            <input type="text" name="sss">
            <input type="submit">
        </form>
    </body>
    </html>
    """

    if request.method == 'GET':
        return HttpResponse(html)
    elif request.method == 'POST':
        sss = request.POST['sss']
        return HttpResponse("post提交 sss =" + sss)
    else:
        return HttpResponse("其他请求方式")


# 社保计算器
def shebao(request):
    if request.method == 'GET':
        return render(request, 'shebao.html')


def shebao_result(request):
    if request.method == 'POST':
        money = request.POST.get('money', 0.00)
        money = money if money else '0'
        money = float(money)
        is_city = request.POST.get('is_city', 0)
        yl_gr = money * 0.08
        yl_dw = money * 0.19
        sy_gr = money * (0.02 if is_city == '1' else 0)
        sy_dw = money * 0.08

        return render(request, 'shebao_result.html', locals())
    else:
        return HttpResponse("请使用post请求方式")


# 调用模板文件
def page1_templates(request):
    '''此函数用于测试模板的加载渲染'''
    # t = loader.get_template("page1.html")
    # html = t.render()
    # return HttpResponse(html)

    # 第二种方式
    return render(request, 'page1.html')


class Dog:
    def __init__(self, k, c):
        self.kinds = k
        self.color = c

    def info(self):
        return self.color + '的' + self.kinds + '狗'


# 模板传参
def page2_render(request):
    d = {'name': '老师',
         'age': 32,
         'favorite': ['看书', '看电影'],
         'friend': {'name': '小张', 'age': 25},
         'pet': Dog('京巴', '白色')}

    # 第一种传参方式
    # t = loader.get_template('page2.html')
    # html = t.render(d)
    # return HttpResponse(html)

    # 第二种传参方式
    return render(request, 'page2.html', d)


def page3(request):
    d = {'name': '老师',
         'age': 32,
         'favorite': ['看书', '看电影', '篮球', '羽毛球', '游戏']
         }
    return render(request, 'page3.html', d)


def page4(request):
    string = 'welcome to SH'
    a = 100
    b = 200
    print('locals=', locals())
    return render(request, 'page4.html', locals())


def homepage(request):
    return render(request, 'base.html')


def sport_homepage(request):
    return render(request, 'sport.html')


def pages(request):
    return render(request, 'pages.html')


def people(request, name):
    return render(request, 'people.html', locals())


def info(request, name):
    s = name + '的详细信息'
    return HttpResponse(s)


def static_test(request):
    return render(request, 'staticTest.html')


def on_upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    elif request.method == 'POST':
        myfile = request.FILES['myfile']
        print('myfile=', myfile)
        print('上传文件的名称为：', myfile.name)

        # 使用setting模块
        with open(os.path.join(settings.UPLOAD_DIR, myfile.name), 'wb') as f:
            b = myfile.file.read()
            f.write(b)# 写入相应位置

        return HttpResponse('文件上传成功')
