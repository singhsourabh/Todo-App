from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import ToDo
from .forms import todoForm

def index(request):
	todoList = ToDo.objects.order_by('id')[::-1]
	form = todoForm()
	context = {'todoList' : todoList, 'forms':form}
	return render(request, 'task/todo.html', context)


def add(request):
	newTask = ToDo(text=request.POST['task'])
	newTask.save()
	return HttpResponse('')

def delete(request):
	remove = ToDo.objects.filter(completed__exact=True).delete()
	return HttpResponse('')

def completed(request, todo_id):
	todo = ToDo.objects.get(pk=todo_id)
	todo.completed = True
	todo.save()
	return redirect('index')