from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from cart.models import Cart_bd
from .forms import LoginForm, UserRegistrationForm
from .models import Profile

from loguru import logger
logger.add("logs/account_logs/log", format="{time} {level} {message}", level="ERROR",
           rotation="1 MB", compression='zip')


@logger.catch
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@logger.catch
def register(request):
    grup_name = "client"
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            my_group = Group.objects.get(name=grup_name)
            my_group.user_set.add(new_user)
            # Create the user profile
            Profile.objects.create(user=new_user)
            Cart_bd.objects.create(user=new_user)
            logger.info("Зарегистрирован новый пользователь!")
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})

