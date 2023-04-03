from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from todolist.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("is_done")
    task_count = Task.objects.count()

    context = {
        "task_count": task_count,
        "tasks": tasks,
    }

    return render(request, "todolist/index.html", context)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")
