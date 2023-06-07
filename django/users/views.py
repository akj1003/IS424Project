from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, SignupForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["confirm_password"]:
                form.save()
                user = form.instance
                user.set_password(form.cleaned_data["password"])
                user.save()

                return redirect('login')

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')
