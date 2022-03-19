from asyncio import all_tasks
from multiprocessing import context
from sre_constants import SUCCESS
from turtle import title
from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html', context)

def tasks(request):
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'tasks.html', context)