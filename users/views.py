from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from users.models import CustomUser, Favorite


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

        # --- Сохранение профиля ---
        if 'profile_submit' in request.POST:
            first_name = request.POST.get('firstname', '').strip()
            last_name = request.POST.get('lastname', '').strip()
            email = request.POST.get('email', '').strip()
            address = request.POST.get('address', '').strip()

            updated = False

            if first_name and first_name != user.first_name:
                user.first_name = first_name
                updated = True

            if last_name and last_name != user.last_name:
                user.last_name = last_name
                updated = True

            if email and email != user.email:
                user.email = email
                updated = True

            if hasattr(user, 'address') and address != user.address:
                user.address = address
                updated = True

            if updated:
                user.save()
                messages.success(request, "Профиль успешно обновлен")
            else:
                messages.info(request, "Изменений не обнаружено")

        # --- Изменение пароля ---
        elif 'password_submit' in request.POST:
            current_password = request.POST.get('current_password', '').strip()
            new_password = request.POST.get('new_password', '').strip()
            confirm_password = request.POST.get('confirm_password', '').strip()

            if not all([current_password, new_password, confirm_password]):
                messages.error(request, "Заполните все поля")
            elif not user.check_password(current_password):
                messages.error(request, "Неверный текущий пароль")
            elif new_password != confirm_password:
                messages.error(request, "Новый пароль и подтверждение не совпадают")
            elif len(new_password) < 8:
                messages.error(request, "Пароль должен быть не менее 8 символов")
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # сохраняем сессию
                messages.success(request, "Пароль успешно изменен")

    # --- Рендер страницы с актуальными данными ---
    return render(request, 'users/profile_edit.html', context={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'address': getattr(user, 'address', ''),
    })


@login_required (login_url='login')
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        favorite.delete()  # если уже был — убираем

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def favorites(request):
    products = Product.objects.filter(favorite__user=request.user).order_by('-id')

    favorite_ids = products.values_list('id', flat=True)

    return render(request, 'users/favorites.html', context= {
        'products': products,
        'favorites': favorite_ids,
    })