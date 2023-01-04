from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . models import User, ChatModel
from . forms import RegisterUserForm, UpdateUserProfile

@login_required
def chat(request, pk):
    user_obj = User.objects.get(pk=pk)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    message_objs = ChatModel.objects.filter(thread_name=thread_name)

    return render(request, 'chat.html', {'user': user_obj, 'msj':message_objs})


@login_required
def home(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'home.html', {'users':users})


@login_required
def update_user(request):
    user = request.user
    form = UpdateUserProfile(instance=user)

    if request.method == 'POST':
        form = UpdateUserProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('home')

    return render(request, 'update_user.html', {'form':form})


def register_page(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Account created!')
            return redirect('home')
        else:
            messages.success(request, 'An error ocurred during registration!')

    return render(request, 'register.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.success(request, 'See you later!')
    return redirect('login_page')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.success(request, 'User does not exist!')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome ' + user.username)
            return redirect('home')

        else:
            messages.success(request, 'Username or password noes not match')

    return render(request, 'login.html')