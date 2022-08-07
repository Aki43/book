from django.forms import ModelForm, TextInput, Textarea, widgets
from dataclasses import fields

from .models import Task, Post


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "Task"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   "Task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})}


class PostForm(ModelForm):
    class Zeta:
        model = Post
        fields = ["title", "body"]
        widgets = {"title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'})}
