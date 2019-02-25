from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name="users/login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:list')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
