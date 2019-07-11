from django.shortcuts import render,HttpResponse
from .models import Item
# Create your views here.

def get_todo_list(request):
    return render(request, "todo_list.html")