from django.shortcuts import render
from django.utils import timezone 
from .models import List
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	todo_items=List.objects.all().order_by("-created_at")
	return render(request, 'base.html',{"todo_items" : todo_items})

def list(request):
	created_at = timezone.now()
	list_item = request.POST.get('list_item')
	List.objects.create(list_item=list_item)
	todo_items=List.objects.all().order_by("-created_at")
	return render(request, 'base.html', {"todo_items" : todo_items})

def delete_item(request, item_id):
	List.objects.get(id=item_id).delete()
	return HttpResponseRedirect("/")

