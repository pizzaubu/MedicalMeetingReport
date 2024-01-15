from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from .models import UserManager

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # สามารถเปลี่ยน URL ไปยังหน้าหลักของคุณได้
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # สามารถเปลี่ยน URL ไปยังหน้าหลักของคุณได้
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def reset_password_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        try:
            UserManager().reset_password(email, new_password)
            return redirect('login')  # หรือหน้าอื่นที่เหมาะสม
        except ValueError as e:
            return render(request, 'reset_password.html', {'error': str(e)})

    return render(request, 'accounts/reset_password.html')


