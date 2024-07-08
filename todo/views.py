from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task_list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tags_list")
