from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


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


def homepage(request):
    html = "这是首页"
    return HttpResponse(html)


def index(request):
    return HttpResponse("这是Index页面")


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
