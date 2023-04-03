from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from todolist.models import Tag, Task
from todolist.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("is_done", "-datetime")
    context_object_name = "tasks"
    template_name = "todolist/index.html"
    paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:index")


def toggle_complete_task(
    request: HttpRequest,
    pk: int
) -> HttpResponseRedirect:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todolist:index"))
