from django.shortcuts import render
from . import models


def index(request):
    todos = models.TodoItem.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'app_todo/index.html', context)
