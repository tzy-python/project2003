from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print('这是第一个视图')
    return HttpResponse("success")

def user(request):
    print('111')

def login(request):
    print('第三个视图')