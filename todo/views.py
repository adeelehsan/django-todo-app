from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone
from .models import Task


def index(request):
    todo_list = Task.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)


def create(request):
    if not request.POST:
        return render(request, 'todo/create.html', {})
    else:
        t = Task(title=request.POST.get('title'), description=request.POST.get('description'), due_date=timezone.now())
        t.save()
        return HttpResponseRedirect(reverse('todo:index'))

def detail(request, todo_id):
    taske = Task.objects.get(id=todo_id)
    context = {'taske': taske}
    return render(request, 'todo/detail.html', context)

def delete(request, todo_id):
    taske = Task.objects.get(id=todo_id)
    taske.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def update(request, todo_id):
    if not request.POST:
        taske = Task.objects.get(id=todo_id)
        context = {'taske': taske}
        return render(request, 'todo/update.html', context)
    taske = Task.objects.get(id=todo_id)
    taske.title=request.POST.get('title')
    taske.description=request.POST.get('description')
    taske.save()
    return HttpResponseRedirect(reverse('todo:index'))