from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from todolist.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    task_count = Task.objects.count()

    context = {
        "task_count": task_count,
        "tasks": tasks,
    }

    return render(request, "todolist/index.html", context)
