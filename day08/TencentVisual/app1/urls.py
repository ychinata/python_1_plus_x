
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path('crawl/(\w+)', views.crawl_data)
]
