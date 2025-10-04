from django.shortcuts import render
from django.views.generic import (TemplateView, View, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .models import Task
from .forms import TaskForm


class Index(TemplateView):
    template_name = "todoapp/task_list.html"


class TaskListView(ListView):
    model = Task
    template_name = "todoapp/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todoapp/task_form.html"
    success_url = "/"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todoapp/task_form.html"
    success_url = "/"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todoapp/task_confirm_delete.html"
    context_object_name = "task"
    success_url = "/"
