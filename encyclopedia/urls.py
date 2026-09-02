from django.urls import path
from . import views


app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random/", views.random_page, name="random"),
    path("add_new/", views.add_page, name="page"),
]
