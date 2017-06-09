# Create your views here.
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .decorators import user_has_perm
from .forms import TaskForm
from .models import Task

@login_required
@user_has_perm
def index(request, todo_list):
    # if request.user.has_perm('todo.can_view'):
    #     todo_list = Task.objects.all()
    # else:
    #     todo_list = Task.objects.filter(user=request.user)
    #todo_list = get_object_or_404(request)
    context = {'todo_list': todo_list}
    return render(request, 'todo/index.html', context)


def create(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return HttpResponseRedirect(reverse('todo:index'))
        else:
            return render(request, 'todo/create.html', {'form': form})
    else:
        return render(request, 'todo/create.html', {'form': TaskForm()})


@require_GET
def detail(request, todo_id):
    try:
        task = Task.objects.get(id=todo_id)
        context = {'taske': task}
        return render(request, 'todo/detail.html', context)
    except (KeyError, Task.DoesNotExit):
        return render(request, 'todo/detail.html', {})


def delete(request, todo_id):
    taske = Task.objects.get(id=todo_id)
    taske.delete()
    return HttpResponseRedirect(reverse('todo:index'))


def update(request, todo_id):
    if not request.POST:
        task = Task.objects.get(id=todo_id)
        form = TaskForm(instance=task)
        context = {'form': form}
        # import pdb;pdb.set_trace()
        return render(request, 'todo/update.html', context)
    task = Task.objects.get(id=int(todo_id))
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todo:index'))
    else:
        return render(request, 'todo/update.html', {'form': form})
