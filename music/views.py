from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def list(request):
    return HttpResponse("music里的list被调用")


def index(request):
    return HttpResponse("music的首页")