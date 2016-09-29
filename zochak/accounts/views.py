from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            authenticated_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            auth_login(request, authenticated_user)
            return redirect("index")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {
        "form": form,
        })
