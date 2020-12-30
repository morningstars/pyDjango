from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models


# Create your views here.

def login(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        resp = render(request, 'login.html', locals())
        return resp
    elif request.method == 'POST':
        # 获取表单数据
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        remember = request.POST.get('remember', '')

        # 验证用户名、密码
        try:
            user = models.User.objects.get(name=username)
            if username == user.name and password == user.password:
                # 登录成功
                request.session['userinfo'] = {
                    'username': user.name,
                    'userId': user.id
                }
                # request.session['username'] = user.name
                # request.session['userId'] = user.id

                # 处理cookie
                resp = HttpResponseRedirect('/userinfo')
                if remember:
                    resp.set_cookie('username', username, 7 * 24 * 60 * 60)
                else:
                    resp.delete_cookie('username')
                return resp
            else:
                return HttpResponse('用户名密码错误！')
        except:
            return HttpResponse('用户未注册')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        name = request.POST.get('username', '')
        psd = request.POST.get('password', '')
        psd2 = request.POST.get('password2', '')

        # 判断用户名密码
        if not name:
            name_error = '用户名不能为空'
        elif psd != psd2:
            password_error = '两次密码不一致'
        else:
            models.User.objects.create(name=name,
                                       password=psd)
            return HttpResponseRedirect('/userinfo/login')
        return render(request, 'register.html', locals())


def logout(request):
    if request.method == 'GET':
        return render(request, 'logout.html', locals())
    else:
        del request.session['userinfo']
        return HttpResponseRedirect('/userinfo')


def homepage(request):
    return render(request, 'homepage.html', locals())
