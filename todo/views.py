from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


