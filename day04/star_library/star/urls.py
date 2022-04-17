from django.urls import path

from . import views

app_name = "star"

urlpatterns = [
    path(r"search", views.SearchView.as_view(), name="search"),
    path(r"register", views.RegisterView.as_view(), name="register"),
    path(r"logout", views.LogoutView.as_view(), name="logout"),
    path(r"login", views.LoginView.as_view(), name="login"),
]
