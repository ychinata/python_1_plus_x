# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SearchForm
from .models import Star
from .models import Star, UserPro


# Create your views here.
class SearchView(View):
    # 当客户端使用get方法发送HTTP请求时，Django会调用这个方法
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        # 实例化表单验证对象
        search_form = SearchForm(request.POST)
        # 进行校验
        if search_form.is_valid():
            # 获取干净的数据
            name = search_form.cleaned_data.get("name")
            # 数据查询
            star = Star.objects.filter(name=name)
            if star:
                return render(request, "detail.html", {"star": star[0]})
            messages.error(request, "你搜索的明星不存在^_^")
        return render(request, "index.html", {
            "search_form": search_form
        })


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        register_form = RegisterView(request.POST)
        if register_form.is_valid():
            nickname = register_form.cleaned_data["nickname"]
            email = register_form.cleaned_data["email"]
            # 获取密码
            password = register_form.cleaned_data["password"]
            # 实例化一个用户对象
            user = UserPro(username=email)
            # 把加密后的密码设置给对象
            user.set_password(password)
            # 邮箱
            user.email = email
            user.nickname = nickname
            user.save()
            # 使用django提供的登录方式
            login(request, user)
            return HttpResponseRedirect(reverse("star:search"))
        else:
            return render(request, "register.html", {
                "register_post_form": register_form
            })
