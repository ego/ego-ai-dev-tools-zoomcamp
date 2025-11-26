from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
    return redirect('index')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
