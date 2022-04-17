from django.urls import path

# 自己写的库和导入的库之间空一行区分开
from . import views

app_name = "star"

urlpatterns = [
    path(r"search", views.SearchView.as_view(), name="search"),
]