import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.db.models import Q, F, Max, Min, Avg, Sum

# Create your views here.


def index1(request):
    return HttpResponse(reverse("courses:index"))


# url传参
# 修改courses/urls.py
def index2(request, v1, v2):
    return HttpResponse(f"视图函数接收到的参数有：{v1}和{v2}")


# index?name=lisa&age=20
def index3(request):
    name = request.GET.get("name", "")
    age = request.GET.get("age", 0)
    user = {"name": name, "age": age}
    # return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")
    # 序列化
    # json_data = json.dumps(user)
    # return HttpResponse(json_data, content_type="application/json", status=404)
    # 如果不想使用JSON模块进行序列化可以使用JsonResponse对象
    return JsonResponse(user)


# 通过form表单提交的参数
def index4(request):
    name = request.POST.get("name", "")
    age = request.POST.get("age", 0)
    return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")


# 通过json提交的参数
def index5(request):
    # 序列化：就是把Python的数据类型转换为JSON字符串
    # 反序列化：就是把JSON字符串转换为Python数据类型
    # 要对JSON数据进行反序列化
    req_data = json.loads(request.body)
    name = req_data["name"]
    age = req_data["age"]
    return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")
