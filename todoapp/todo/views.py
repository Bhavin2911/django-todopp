from django.shortcuts import render
from .models import todoitem
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	all_items=todoitem.objects.all()
	return render(request,'index.html',{'all_items':all_items})

def	addtodo(request):
	newitem=todoitem(content=request.POST['content']) 
	newitem.save()
	return HttpResponseRedirect('/')

def	deletetodo(request,todo_id):
	delete_item = todoitem.objects.get(id=todo_id)
	delete_item.delete()
	return HttpResponseRedirect('/')	