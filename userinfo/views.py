from django.shortcuts import render


# Create your views here.

def login(request):
    resp = render(request, 'login.html', locals())
    if request.method == 'POST':
        resp.set_cookie('username', request.POST.get('username', ''))
        resp.set_cookie('password', request.POST.get('password', ''))
        resp.set_cookie('remember', request.POST.get('remember', ''))
    return resp
