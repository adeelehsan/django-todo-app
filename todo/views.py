# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.models import Permission
from .models import Task


def index(request):
    if request.user.has_perm('can view all task'):
        print "I was there"
    else:
        todo_list = Task.objects.filter(user=request.user)
    todo_list = Task.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)


def create(request):
    if not request.POST:
        return render(request, 'todo/create.html', {})
    else:
        t = Task(title=request.POST.get('title'), description=request.POST.get('description'))
        t.user = request.user
        t.save()
        return HttpResponseRedirect(reverse('todo:index'))


def detail(request, todo_id):
    task = Task.objects.get(id=todo_id)
    context = {'taske': task}
    return render(request, 'todo/detail.html', context)


def delete(request, todo_id):
    taske = Task.objects.get(id=todo_id)
    taske.delete()
    return HttpResponseRedirect(reverse('todo:index'))


def update(request, todo_id):
    if not request.POST:
        task = Task.objects.get(id=todo_id)
        context = {'taske': task}
        return render(request, 'todo/update.html', context)
    task = Task.objects.get(id=todo_id)
    task.title = request.POST.get('title')
    task.description = request.POST.get('description')
    task.save()
    return HttpResponseRedirect(reverse('todo:index'))
