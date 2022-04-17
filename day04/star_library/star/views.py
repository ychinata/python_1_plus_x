# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .forms import SearchForm, LoginForm, RegisterForm
from .models import Star, UserPro


# Create your views here.
class SearchView(LoginRequiredMixin, View):
    login_url = "/star/login"

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
        # 实例化一个表单对象
        register_form = RegisterForm(request.POST)
        # 判断校验是否通过
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
            # 昵称
            user.nickname = nickname
            # 保存
            user.save()
            # 使用django提供的登录方式
            login(request, user)
            return HttpResponseRedirect(reverse("star:search"))
        else:
            return render(request, "register.html", {
                "register_post_form": register_form
            })


# 自定义用户校验方法
class CustomAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserPro.objects.get(Q(username=username) | Q(nickname=username) | Q(email=username))
            is_valid = user.check_password(password)
            return user if is_valid else None
        except Exception as e:
            print(e)
            return None


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        # 实例化一个表单验证对象
        login_form = LoginForm(request.POST)
        # 进行验证
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 应该把密码加密，加密后和数据库里面的密码进行匹配
            # 使用django提交检验方式
            user = authenticate(username=username, password=password)
            if user is not None:
                # 说明用户名和密码匹配
                # 登录
                login(request, user)
                # 为了用户的体验，我们应该登录完成后跳转到用户所访问的页面
                next_page = request.GET.get("next", "")
                if next_page:
                    return HttpResponseRedirect(next_page)
                return HttpResponseRedirect(reverse("star:search"))
            else:
                return render(request, "login.html", {
                    "msg": "用户名或密码错误"
                })
        else:
            return render(request, "login.html", {
                "login_form": login_form
            })


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("star:search"))
		
