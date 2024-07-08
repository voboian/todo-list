from django.urls import path
from .views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tags/", TagListView.as_view(), name="tags_list"),
]

app_name = "todo"
