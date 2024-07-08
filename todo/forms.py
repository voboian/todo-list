from datetime import datetime, date

from django import forms
from django.core.exceptions import ValidationError

from .models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
        }

    def clean_deadline(self) -> datetime:
        task_deadline = self.cleaned_data["deadline"]

        if task_deadline < date.today():
            raise ValidationError("Please, select date in future")

        return task_deadline


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
