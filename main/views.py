from idlelib.rpc import request_queue

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request

from django.views import *
from .models import *


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:

            tasks = Task.objects.filter(owner=request.user)



            context = {
                'STATUS_CHOICES': Task.STATUS_CHOICE,
                'tasks': tasks
            }
            return render(request,'index.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            deadline = request.POST.get('deadline')
            if deadline == "":
               deadline = None

            details = request.POST.get('details')
            if details == "":
               details = None

            Task.objects.create(
                title=request.POST.get('title'),
                details=details,
                status=request.POST.get('status'),
                deadline=deadline,
                owner=request.user
            )

            return redirect('index')
        return redirect('login')

class UpdateView(View):
    def get(self,request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=pk, owner=request.user)
            context = {
                'task': task,
                'STATUS_CHOICES': Task.STATUS_CHOICE,
            }

            return render(request,'edit.html', context)
        return redirect('login')


    def post(self, request, pk):
        if request.user.is_authenticated:
            task  =get_object_or_404(Task, id=pk, owner=request.user)
            Task.objects.filter(id=pk).update(
                title=request.POST.get('title'),
                details=request.POST.get('details'),
                status=request.POST.get('status'),
            )
            return redirect('index')
        return redirect('login')

class DeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, pk=pk, owner=request.user)
            task.delete()
            return redirect('index')
        return redirect('login')




class RegisterView(View):
    def get(self, request):
        return render(request,'register.html')


    def post(self,request):
        if request.POST.get('password1') == request.POST.get('password2'):
            if request.POST.get('username') in User.objects.values_list('username',flat=True):
                return redirect('register')
            User.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password1')
            )
            return redirect('login')
        return redirect('register')


class LoginView(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('index')
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')




