from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms

from django.contrib import messages
from .models import User_accounts
from django.forms import ModelForm

from .forms import SignUpForm

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
			#group = Group.objects.get(name='Customer')
			#user.groups.add(group)
			
            form.save()

			

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('eMahei')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'signin.html', context)

def logoutUser(request):
	logout(request)
	return redirect('eMahei')


