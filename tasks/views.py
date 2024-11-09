from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import AddTaskForm, EditTaskForm

def task_list(request):
    tasks = Task.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        tasks = tasks.filter(categories__id=category_id)

    categories = Category.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'categories': categories})

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:task_list')