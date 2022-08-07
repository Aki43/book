from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Post
from .forms import TaskForm, PostForm

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/main_index.html',{'title': 'Главная страница','tasks': tasks})

def about(request):
    posts = Post.objects.all()
    return render(request,'main/about.html',{'title1': 'Страница про нас','posts': posts})

def ukraine(request):
    form1 = PostForm()
    context = {'form1':form1}
    return render(request,'main/ukraine.html', context)

def create(request):
    error =''
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была не верной"
    form = TaskForm
    context = {'form':form, 'error': error}
    return render(request,'main/create.html', context)