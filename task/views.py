from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import ToDo
from .forms import todoForm

def index(request):
	todoList = ToDo.objects.order_by('id')[::-1]
	form = todoForm()
	context = {'todoList' : todoList, 'forms':form}
	return render(request, 'task/todo.html', context)

@require_POST
def add(request):
	form = todoForm(request.POST)
	if form.is_valid():
		newTask = ToDo(text=request.POST['text'])
		newTask.save()
	return redirect('index')

def delete(request):
	remove = ToDo.objects.filter(completed__exact=True).delete()
	return redirect('index')

def completed(request, todo_id):
	todo = ToDo.objects.get(pk=todo_id)
	todo.completed = True
	todo.save()
	return redirect('index')