from django.http import HttpResponse
from django.http import HttpResponseNotFound
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


def shebao(request):
    html = """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form method="post" action="/shebao">

    请输入基数：
    <input type="text" name="salary">
    <p>
        请选择户口：
        <select name="country">
            <option value="city">城镇人口</option>
            <option value="town">农村人口</option>
        </select>
    </p>
    <input type="submit">
</form>
</body>
</html>
    """
    if request.method == 'GET':
        return HttpResponse(html)
    elif request.method == 'POST':
        html = """
        
        <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<table>
    <thead>
        <tr>
            <td>项目</td>
            <td>个人缴纳</td>
            <td>单位缴纳</td>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>养老保险</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>失业保险</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>工伤保险</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>生育保险</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>医疗保险</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>公积金</td>
        <td>xxxx元</td>
        <td>xxxx元</td>
    </tr>
    <tr>
        <td>个人缴费总和</td>
        <td colspan="2">xxxx元</td>
    </tr>
    <tr>
        <td>公司缴费总和</td>
        <td colspan="2">xxxx元</td>
    </tr>
    <tr>
        <td>纳入国家全额总和</td>
        <td colspan="2">xxxx元</td>
    </tr>
    </tbody>

</table>

</body>
</html>
        
        """
        value = request.POST.get('salary', 0.00)
        hukou = request.POST.get('country', '')
        print("基数：" + value + " 户口：" + hukou)
        return HttpResponse(html)
    else:
        return HttpResponse("其他")


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
