from django.http import HttpResponse
from django.shortcuts import redirect, render
from todolist_app.models import TaskList, Contact
from todolist_app.forms import TaskForm, ContactForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
           instance = form.save(commit=False)
           instance.owner = request.user
           instance.save()
        messages.success(request,('New Task Added!'))
        return redirect('Todolist')
    else:
        all_tasks = TaskList.objects.filter(owner = request.user)
        paginator = Paginator(all_tasks, 10)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks' : all_tasks})

@login_required    
def delete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.owner == request.user:
        task.delete()
        messages.success(request,('Task Deleted Successfully!'))
    else:
        messages.error(request,('Access Restricted, You are not allowed to change!'))
    return redirect('Todolist')

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
           form.save()
        messages.success(request,('Task Edited!'))
        return redirect('Todolist')
    else:
        task_obj = TaskList.objects.get(pk = task_id)
        return render(request, 'edit.html', {'task_obj' : task_obj})

@login_required    
def complete_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
        messages.success(request,('Task Status Changed Successfully!'))
    else:
        messages.error(request,('Access Restricted, You are not allowed to change!'))
        
    return redirect('Todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.owner == request.user:
       task.done = False
       task.save()
       messages.success(request,('Task Status Changed Successfully!'))
    else:
        messages.error(request,('Access Restricted, You are not allowed to change!'))
    return redirect('Todolist')
    
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
           form.save()
           messages.success(request,('Message Sent!'))
        return redirect('Todolist')
    return render(request, 'contact.html')

def about(request):
    context = {
        "HomePage" : "Task Planner is a task management tool. Our aim to keep you updated about your day to day Tasks.",
    }
    return render(request, 'about.html', context)