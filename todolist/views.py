from operator import truediv
from todolist.models import *
from todolist.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.core import serializers


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    if request.user.is_authenticated:
        user = request.user
    data_todolist_item = ToDoTask.objects.filter(task_user = user)
    context = {
        'username': request.user.username,
        'list_item': data_todolist_item,
    }
    return render(request, "todolist.html", context)


def show_json(request):
    if request.user.is_authenticated:
        user = request.user
    data = ToDoTask.objects.filter(task_user = user)
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")
    
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_user = request.user
            task.save()
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def update_finish(request, id):
    object = get_object_or_404(ToDoTask, pk = id)
    object.task_isfinished = not object.task_isfinished
    object.save()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def update_delete(request, id):
    object = get_object_or_404(ToDoTask, pk = id)
    object.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = request.user
            task = form.save(commit=False)
            task.task_user = request.user
            task.save()
            data = ToDoTask.objects.filter(task_user = user)
            return HttpResponse(serializers.serialize("json", data), \
                content_type="application/json")
    else:
        form = TaskForm()
    return render(request, 'todolist.html', {'form': form})
