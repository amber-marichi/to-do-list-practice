from django.urls import path

from todolist.views import (
    index,
    TagListView,
    TagCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    )
]

app_name = "todolist"
