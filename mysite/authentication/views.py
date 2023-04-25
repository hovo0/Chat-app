# authentication/views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'chat/index.html')
        else:
            return render(request, 'authentication/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'authentication/login.html')
