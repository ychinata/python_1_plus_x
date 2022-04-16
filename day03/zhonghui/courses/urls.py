from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path(r"index", views.index, name="index"),  # 在views.py里定义
    # path(r"create", views.create, name="create"),
    # path(r"update/<str:name>", views.update, name="update"),
    # path(r"delete/<str:name>", views.delete, name="delete"),
    path(r"index/<int:v1>/<int:v2>", views.index, name="index"),
]
