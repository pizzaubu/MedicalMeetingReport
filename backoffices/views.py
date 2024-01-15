from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AdminLoginForms
from accounts.models import User

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                # Handle login error
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials or not an admin.'})
    else:
        form = AdminLoginForms()

    return render(request, 'login.html', {'form': form})