from django.urls import path

from .views.main_views import home, single_blog
from .views.auth_views import register, login
from .views.main_views import create_blog, edit_blog, single_blog
urlpatterns = [
    path("/", home),
    path("register/", register),
    path("login/", login),
    path("create-blog/", create_blog),
    path("edit-blog/", edit_blog),
    path("single-blog/<int:id>", single_blog)
]
