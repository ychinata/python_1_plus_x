from django.urls import path

from . import views

app_name = "star"

urlpatterns = [
    path(r"search", views.SearchView.as_view(), name="search"),
]
