from django.urls import path
from . import views


app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit_page, name="edit"),
    path("random/", views.random_page, name="random"),
    path("new_entry/", views.add_page, name="page"),
    path("search/", views.search, name="search"),
]
