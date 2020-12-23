from django.http import HttpResponse


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

def index(resquest):
    return HttpResponse("这是Index页面")

