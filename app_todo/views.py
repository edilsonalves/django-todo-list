from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models


def index(request):
    todos = models.TodoItem.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'app_todo/index.html', context)


def create(request):
    todo = models.TodoItem()
    todo.content = request.POST['content']
    todo.save()

    return HttpResponseRedirect('/')


def delete(request, todo_id):
    todo = models.TodoItem.objects.get(id=todo_id)
    todo.delete()

    return HttpResponseRedirect('/')
