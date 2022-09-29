from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/wishlist/login/')
def show_todolist(request):
        data_todolist = Task.objects.all()
        context = {
                'todolist': data_todolist,
                'nama': 'Sania Rizqi Maharani',
                'student_id': '2006597001',
                'last_login': request.COOOKIES['last_login'],
        }
        return render(request, "todolist.html", context)

def register(request):
        form = UserCreationForm()

        if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Akun telah berhasil dibuat!')
                        return redirect('todolist:login')
        
        context = {'form':form}
        return render(request, 'register.html', context)

def login_user(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
                        response.set_cookie('last_login', str(datetime.datetime.now())) 
                        return response
                else:
                        messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)

def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login'))
        response.delete_cookie('last_login')
        return response

def add_task(request):
        form = TaskForm(request.POST)

        if request.method == "POST":
                form = TaskForm(request.POST)
                if form.is_valid():
                        save_data = Task.objects.create(
                                title = form.cleaned_data.get('title'),
                                description = form.cleaned_data.get('description')
                        )
                        form.save(commit=False)
                        
                        messages.success(request, 'Task telah berhasil ditambahkan!')
                        return redirect('todolist:show_todolist')
    
        context = {'form':form}
        return render(request, 'addtask.html', context)
