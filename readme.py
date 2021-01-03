"""
day01
 Django 安装
  创建 Django 项目的命令
    $ django-admin startproject 项目名称

    项目名称/
        manage.py  # 开发运行和调用的主模块
        项目名称（包）
              __init__.py
              settings.py  # 配置文件
              urls.py      # 定义路由指定视图函数
              wsgi.py      # 用于uwsgi部署
    HTTP:
           http://127.0.0.1:8000/page1
        请求  ------>    服务器
             <------
                 响应
        请求 Request
        响应 Response
    # file : urls.py
       urlparttens = [
            url(r"^index", 视图函数)，
            url(r"^year/(\d{4})/(\d{1,2})",
               视图函数2),
            url(r"^person/(?P<name>\w+)",
               视图函数3)，
       ]
        # def 视图函数2(request, a, b):
        # def 视图函数3(request, name):
        # def 视图函数3(request, **kwargs):
    # file : views.py
    def 视图函数名(reqeust):
         .....
        return 响应对象(...) # HttpResponse,...
    HTTP请求方式：
        GET
        POST
        HEAD
        PUT
        DELETE
        def view1(request):
            if reqeust.method == 'GET':
                value = request.GET[键]
            elif request.method == 'POST':
                try:
                    value = request.POST[键]
                except:
                    value = 0
                value = reqeust.POST.get(键，0)
    request.COOKIE
    request.session
    request.path
    request.path_info
    ....

响应
  状态码：
    1xx
    2xx     成功
    3xx     重定响
    4xx     客户端错误
    5xx     服务器端错误
  HttpResponse(请求体的内容， content_type, 状态码默认是200)
  return HttpResponse("页面1")

"""

"""
day02
MVC / MTV设计模式
  模板 template
     1. 模板的配置
        setting.py
         TEMPLATE = [
            DIRS = [...模板的绝对路径1,路径2,...]
            ....
         ]
         DEBUG = True/False
    2. 模板的加载方法：
       1.  from django.shortcut import render
           render(request, '模版的相对路径名', 数据字典)
           render 返回的是一个HttpResponse对象
       2. from django.template import loader
          t = loader.get_template('模版的相对路径名')
          html = t.render(数据字典)
          return HttpResponse(html)

    3. 模板的语法：
        模板的变量
            {{ 变量名 }}
            {{ 变量名.1 }}
            {{ 变量名.key}}
            {{ 对象.方法 }}
        模板的控制标签
            if 标签
                {% if 条件表达式 %}
                {% elif .... %}
                {% else %}
                {% endif %}
            for 标签
                {% for x in 可迭代对象 %}
                ... {{ forloop.counter }}
                {% empty %}
                {% endfor %}
            cycle 标签
               {% cycle 值1 值2 值3 %}
            注释　
            　　{# #}
                {% comment %}
                {% endcomment}
        模板的过滤器
           {{ 变量 | 过滤器１: 参数1 | }}
        转义　
        　　　{% autoescape on %}
                {{  变量　}}
             {% endautoescate %}
        模板的继承
            {% block 块名　%}

            {% endblock %}

            继承语法
            {% extends '父模板的名称' %}
              {# 覆盖block #}
            {% block 块名　%}
                子模板的新内容
            {% endblock %}
        反向解析
            url(正则表达式，　视图函数，name='别名')
            {% url '别名' %}
            {% url '别名'  '参数1' ...}

"""

"""
day03
  1. 静态文件
  2. Django中的应用
  3. 模型和数据库
  4. 数据库的操作

1. 静态文件
   图片   .js文件  .css 文件 ...
   1. 配置静态文件存放的目录
       mkdir <项目主目录>/static
   2. 在settings.py 里配置这个目录
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, "static"),
        ]
   3. 指定URL路由
       settings.py
       STATIC_URL = '/static/'
2. Django中的应用
   有模型，模板，视图，子路由这样的一个子包
    1. 创建应用
       $ python3 manage.py startapp <应用名称>
    2. <应用名称>/
        migrations/ 文件夹 存放迁移文件
            0001_init....py  
        __init__.py  包中的初始化文件(必须存在)
        views.py   存放视图函数的文件
        tests.py   测试用文件
        models.py  存放数据库模型类的文件(ORM)
            class Book(models.Model)
        templates/  用来存放当前应用自己的模板
             MTV-模型，模板，视图
        admin.py  应用的后台管理模块
        apps.py 应用的属性的配置文件
        urls.py  内部存放自己的分支路由
           urlpatterns = [
               url('分支路由正则', 视图函数)
           ]
    3. 配置安装 应用 在settings.py 中
        INSTALLED_APPS = [
            ....
            '自定义的应用名称'
        ]

3. 模型和数据库
   ORM  
      对象 <------>  关系型数据库
        类            表
        对象          记录
    
    1. 配置MySQL数据库
        1. 创建数据库
        create databases 数据库名
            default charset utf8
            collate utf8_general_ci;
        
        2. 配置数据库 
          将PORT, HOST, USER, PASSWORD
            DATABASES = {
                'default': {
                    "HOST": "127.0.0.1"
                    ...
                }
            }

    2. 数据库的迁移
       $ python3 manage.py makemigrations
       $ python3 manager.py migrate
       注: 如果修改了模型类，就一定要做迁移操作

4. 模型 
   创建数据表  在 <应用名称>/models.py 里
   创建继承是models.Model类的 新类
      class Book(models.Model):
          title = CharField(....)
          pub = CharField(....)
    迁移后会在数据库内生成对应的
       应用名称_book 数据表
          id   自增整数
          title
          pub   

    字段的类型:
       CharField("名称", max_length=50)
       BooleanField(...)
       DateField   存放日期
       DateTimeField 存放日期时间
       DecicmalField 存放浮点数
              max_digits  最大长度
              decimal_palces 小数点后的位数
       FloatField  存放浮点数  float类型 
       EmailField  存放邮箱地址(CharField)
       TextField  长文本
       ...

    3. Django的离线文档
        1. 解压缩数据包
        django-docs-1.11-en.zip
        2. 用浏览器打开
        django-docs-1.11-en/index.html

    4. 字段选项
       null = True/False
       default = ''  缺省值
       primery_key = True/False 主键
       unique  = True/False
       db_index = True/False  # 索引 

数据库的 CRUD
    1. 创建数据记录
       Book.objects.create(title='C++'..)
       book = Book()
       book.title = 'C++'
       book.save()
"""

"""
day04
1. 管理器对象
    class MyBook(models.Model):
          ...
    MyBook.objects  <<管理器对象
2. 管理器对象有很多方法:
    abook = MyBook.objects.create()   创建一条记录
            abook = MyBook()
            abook.title = 'C++'
            abook.save()
    books = MyBook.objects.all()
      查询集合里存的是 MyBook 类型的对象
    books = MyBook.objects.values('title', 'id')     
      查询集合内存的是字典
    books = MyBook.objects.values_list(...)
      查询集合内部存的是 元组
    books = MyBook.objects.order_by('pub','-id')
      返回查询结果集 存MyBook类型的对象 

    books = MyBook.objects.filter(pub='北大..', id__gt=3)
      返回存有MyBook对象的查询结果集

    abook = MyBook.objects.get(pub='北大...')
    books = MyBook.objects.exclude(条件)

字段查找
   可以在 filter(), exclude(), get()
       加入查询谓词
    pub__contains = '北大'
    age__gte = 18   成年人

3. 修改数据记录
    1. 修改单个
    abook = MyBook.objects.get(id=1)
    abook.title = "机械..."
    abook.save()

    2. 修改多个
    books = MyBook.objects.all()
    books.update(price=100)

删除数据记录:
    # 删除一条记录
    abook = ..... get(id=1)
    abook.delete()
    # 删除查询结果集中的全部数据记录
    books = ......all()
    books.delete()

聚合查询
  聚合函数:
    from djang.db.models import \
        Avg, Count, Max, Min, Sum
  不带分组:
     result = MyBook.object.aggregate(
         myAvg=Avg('price')
     )
     print(result)  {"myAvg": 50.8}

  带分组
    pub_set = MyBook.object.values("pub")
           QuerySet[{pub:...}]
    pub_set.annotate(myCount=Count('pub'))

F对象示意代码:
    更新Book实例中所有的制场价涨10元
    books = models.Book.objects.all()
    for book in books:
        book.market_price = book.market_price + 10
        book.save()
    #
    books.update(market_price=F('market_price') + 10)



    1. 创建数据库
        create database ....
    2. 迁移
        python3 manage.py makemigrateions
        python3 manage.py migrate
    3. python3 manage.py runserver


pyCharm 社区版 针对Django项目方法
    1. 添加自己调式配置
        选择 Add Configuration...
    2. 点击+号 添加一个自己的配置
    3. 选择运行的项目的主模块位置 manage.py
    4. 添加 runserver 命令行参数

"""

"""
day05
F 对象
    执行某条记录的相应的字段的操作
    F('pub')
  Q 对象:
    逻辑 与 &
    逻辑 或 |
    逻辑 非 ～
    Q(price__gt＝30) | Q(pub='清华...')

原生的数据库操作
  1. 查询
     模型类.objects.raw('SQL语句')
  2. 其它操作要游标 cursor
    from django.db import connection
    with connection.cursor() as xxx:
       xxx.execute('SQL语句')

admin 后台数据库管理
路由:
   127.0.0.1:8000/admin
创建管理员帐户
   $ python3 manage.py createsuperuser

将自定义的模型类加入到后台管理
　　　<App文件夹下>/admin.py
     # 注册自定义的模型类
       admin.site.register(自定义模型类,
       　　　　　　　　　　　　模型管理器类)
　　 ＃　定义模型管理器类
     # from django.contrib import admin
    class BookManager(admin.ModelAdmin):
        list_display = ['title', ...]
        list_display_links = ['title']
        search_field 
        list_filter 
        list_editable
    

自定义表名管理
    bookstore/models.py
    class Book(models.Model):
        # 'bookstore_book'
        class Meta:
            db_table = 'mybook'


数据表的关联关系映射
  一对一
     class A(models.Model):
         pass

    class B(models.Model):
        mya = models.OneToOneField(A)
    a = A()
    b = B(mya=a)
    正向: 由B找A
       b.mya
    反向: 由A找B
       a.b
  一对多
    class A(models.Model):
        pass

    class B(models.Model):
       mya = models.ForeignKey(A)
    a = A()
    b1 = B(mya=a)
    b2 = B(mya=a)
    多对一查找:
       b1.mya  # 找到A对象
    一对多查询
       items = a.b_set.all()
       #另外一种一对多的查找方法
       items = B.objects.filter(mya=a)
"""

"""
day06
数据表关联关系映射
    关系型数据库
        Oracle
        IBM  DB2
        Microsft SQL Server
    关系表的建立
      一对一
      一对多
        class Grade(...):
            ..
        class Banji(...):
            grade= models.ForeignKey(Grade)
            master = models.ForeignKey(User)
           
      多对多
        class Author(...):
             ....
        class Book(...)
             author = models.ManyToMany(Author)

        a = Author()
        b = Book()
        a.book_set.add(b)

        由收书找作者:
            b.author.all()
        由作者找书
            a.book_set.all()


    多对多其它表现形式:
      class Student(models.Model):
          name = models.CharField('姓名')
        
      class Subject(models.Model):
           title = models.CharField('学科')
    
      class StudentScore(models.Model)
          student = Model.ForeignKey(Student)
          subject = Model.ForeignKey(Subject)
          score = models.IntegerField('成绩')

      xiaozhang = Student.objects.create(
                 name='小张')
      xiaoli = Student.objects.create(
                 name='小李')

      yuwen = Subject.objects.create(
          title='语文')
      shuxue = Subject.objects.create(
          title='数学')
      英语 = Subject.objects.create(
          title='英语')

cookes  浏览器端的存储方式
  键值对方式存储
    resp = HttpResponse()
    resp.set_cookie(key, 值, max_age, ...)

session 服务器端的存储方式
    request.session['userinfo'] = {
        'username': user.name
        'id' : user.id
    }
    request.session.get('userinfo', None)
   在浏览器端加会加一个COOKIE
       sessionid='xxxxxyyyyzzyyaaa'

"""

"""
day07
中间件
  Form 模块
  分页

中间件
浏览器---> 
    |                    |
process_request     process_response
    |
  urls.py
    |
process_view
    |
   views.py

CSRF 跨站点请求伪造
  {% csrf_token %}
  注册  csrf  中间件

分页
   Paginator
   Page
   page = myPaginator.page(11)

Form 模块有两个功能
   用类来生成表单
   表单验证工作
    class RegForm(forms.Form)
        aaa = forms.CharField(label='xx')
        bbb = forms.CharField(...)
    myform = RegForm()
    # 自动解析表单
    myform.as_p()
    {{ myform.as_p }}
    myform.as_ul()
    myform.as_table
    # 手动解析
    {% for f in myform %}
        {{f.label}}  <label>
        {{f}}   <input>



    表单验证:
      myform = RegForm(request.POST)
      if myform.is_valid():
        dic = myform.cleaned_data  表单数据

    class RegForm(forms.Form)
        aaa = forms.CharField(label='xx')
        bbb = forms.CharField(...)

        def clean_aaa(self):
            return 返回aaa数据或触发错误
        def clean(self):
            全局验证
            return self.cleaned_data
"""
"""
day08

1.文件上传
2.django的用户认证机制

"""