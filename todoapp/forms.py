from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "is_completed"]

        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your tasks"}),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "content": "",
            "is_completed": "Completed",
        }
