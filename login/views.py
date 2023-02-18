from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages

from login.decoratos import *
from login.models import Users
from login.forms import CreateUserForm



@unauthenticated_user
def registerUser(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='admin')
			user.groups.add(group)
            
			Users.objects.create(
				user=user,
				nombre=user.username,
				)

			messages.success(request, 'Una cuenta ha sido creada ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('createemp')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')