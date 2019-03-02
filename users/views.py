from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from users.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models, forms
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

class SignUpView(CreateView):
    model = User
    template_name = "users/user_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        _object = form.save()
        models.Profile.objects.create(user=_object)
        return super(SignUpView, self).form_valid(form)


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('users:update_profile')

    def get_object(self):
        return self.request.user.profile

        

        


