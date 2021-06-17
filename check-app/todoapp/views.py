from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.duedate = request.GET['duedate']
    obj.duetime = request.GET['duetime']
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)


def delete(request, id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)


def list(request):
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)


def sortdata(request):
    mydictionary = {
        "alltodos": Todo.objects.all().order_by('-priority')
    }

    return render(request, 'list.html', context=mydictionary)


def sbyd(request):
    mydictionary = {
        "alltodos": Todo.objects.all().order_by('duedate')
    }
    return render(request, 'list.html', context=mydictionary)


def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos": Todo.objects.filter(title__contains=q)
    }
    return render(request, 'list.html', context=mydictionary)


def edit(request, id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title": obj.title,
        "description": obj.description,
        "priority": obj.priority,
        "duedate": obj.duedate,
        "duetime": obj.duetime,
        "id": obj.id
    }
    return render(request, 'edit.html', context=mydictionary)


def update(request, id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.duedate = request.GET['duedate']
    obj.duetime = request.GET['duetime']

    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos": Todo.objects.all()
    }
    return render(request, 'list.html', context=mydictionary)
