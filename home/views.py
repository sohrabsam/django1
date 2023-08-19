from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Todo
from .forms import TodoCraeteForm, TodoUpdateForm


# Create your views here


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'all': all})


def seyhello(request):
    person = {'name': 'admin'}
    return render(request, 'hello.html', context=person)


def detile(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'd.html', context={'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'delete todo', 'success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCraeteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'add data to tabel', 'success')
            return redirect('home')
    else:
        form = TodoCraeteForm()
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form= TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'update data in tabel', 'success')
            return redirect('ditle', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
        return render(request, 'update.html', context={'form': form})
