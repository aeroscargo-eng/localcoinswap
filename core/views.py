# core/views.py
from core.models import TransactionReceipt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index_view(request):
    receipt = TransactionReceipt.objects.last()  # or get(id=1)
    return render(request, 'core/index.html', {'receipt': receipt})


def index2_view(request):
    return render(request, 'core/index2.html')  # Render index2.html

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index after successful login
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})

    return render(request, 'core/login.html')

