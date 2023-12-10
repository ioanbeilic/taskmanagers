from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.id_valid():
            user = form.save()

            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, "signup.html", {'form': form})


def signin(request):
    return render(request, "signin.html")
