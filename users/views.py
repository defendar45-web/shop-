from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import CustomUser


# Регистрация

def register(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            if not CustomUser.objects.filter(email=email).exists():
                CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                return redirect('login')
            else:
                error = "Пользователь с таким именем или почтой уже существует"
        else:
            error = "Заполните все поля"

        return render(request, "users/register.html", {"error": error})

    return render(request, "users/register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                user_login (request, user)
                return redirect("home")
            else:
                error = "Неверный логин или пароль"
        else:
            error = "Заполните поля"
            print(error)

        return render(request, "users/login.html", {"error": error})
    return render(request, "users/login.html")

@login_required(login_url='login')
def profile(request):
   user = request.user

   return render(request, 'users/profile.html', context={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address': user.address,
})

@login_required(login_url='login')
def auth_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            first_name = request.POST['firstname']
            if first_name:
                user.first_name = first_name

            last_name = request.POST['lastname']
            if last_name:
                user.last_name = last_name

            email = request.POST['email']
            if email:
                user.email = email

            address = request.POST['address']
            if address:
                user.address = address

      

            user.save()

            return redirect('profile')

        elif 'password_submit' in request.POST:
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']

            if not user.check_password(current_password):
                messages.error(request, "Неверный текущий пароль")

            elif new_password != confirm_password:
                messages.error(request, "Новый пароль и пароль подтверждения не совпадают.")

            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)

                return render(request, 'users/profile.html', context={
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                })
    return render(request, 'users/profile_edit.html', context={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    })