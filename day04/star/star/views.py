from django.shortcuts import render
from django.views.generic.base import View
# from

from .forms import SearchForm
from .models import Star


# Create your views here.
# 使用Django的父类（基类）
class SearchView(View):
    # 当客户端使用get方法发送HTTP请示时，Django会调用这个方法
    def get(self, request, *args, **kwargs):
        # 打包成字典
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        # 表单对象
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            name = search_form.cleaned_data.get("name")
            star = Star.objects.filter(name=name)
            if star:
                return render(request, "detail.html", {"star": star[0]})

        return render(request, "index.html", {
            "search_form": search_form
        })
