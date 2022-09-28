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

@login_required(login_url='/wishlist/login/')
def show_todolist(request):
        data_todolist = Task.objects.all()
        context = {
                'todolist': data_todolist,
                'nama': 'Sania Rizqi Maharani',
                'student_id': '2006597001',
                
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
                        return redirect('todolist:show_todolist')
                else:
                        messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)

def logout_user(request):
        logout(request)
        return redirect('todolist:login')

def add_task(request):
        form = TaskForm(request.POST)

        if request.method == "POST":
                form = TaskForm(request.POST)
                if form.is_valid():
                        # Task.user = request.user
                        form.save(commit=False)
                        # form.save_m2m()
                        messages.success(request, 'Task telah berhasil ditambahkan!')
                        return redirect('todolist:show_todolist')
    
        context = {'form':form}
        return render(request, 'addtask.html', context)
