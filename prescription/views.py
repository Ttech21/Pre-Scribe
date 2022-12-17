from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            try:
                User.objects.get(username=user.username)
                form = CustomUserCreationForm(request.POST)
                context = {
                    'page': page,
                    'form': form
                }
                return render(request,'prescription/login-register.html', context)
            except ObjectDoesNotExist:
                user.save()
                login(request,user)
                return redirect('login')
        else:
            form = CustomUserCreationForm(request.POST)
            context = {
                'page': page,
                'form': form
            }
            return render(request, 'prescription/login-register.html', context)
    context={
        'page':page,
        'form':form
    }
    return render(request,'prescription/login-register.html',context)


def login_user(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('login')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return redirect('login')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("login")
        else:
            return redirect('login')
    context={
        'page':page
    }
    return render(request,'prescription/login-register.html',context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')



