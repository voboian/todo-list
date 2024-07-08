from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tag/new/", TagCreateView.as_view(), name="tag_new"),
    path("tag/<int:pk>/edit/", TagUpdateView.as_view(), name="tag_edit"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todo"
