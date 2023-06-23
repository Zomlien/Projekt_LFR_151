from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import logging


logger = logging.getLogger(__name__)


def login_user(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe_list')
            else:
                logger.error("Error logging in. Invalid credentials.")
                messages.success(request, "Error logging in, try again.")
                return redirect('login')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    try:
        logout(request)
        messages.success(request, ("You were logged out"))
    except Exception as e:
        messages.error(request, ("An error occurred during logout. Please try again later."))
        raise e
    return redirect('')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save(commit=False)

                is_superuser = request.POST.get('is_superuser', False)
                if is_superuser:
                    user.is_superuser = True
                    user.is_staff = True

                user.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, ("You were successfully registered!"))
                return redirect('recipe_list')
        except Exception as e:
            messages.error(request, ("An error occurred during registration. Please try again later."))
            raise e
    else:
        form = UserCreationForm()

    return render(request, 'registration/register_user.html', {
        'form': form,
    })


@login_required
def view_user(request):
    user = request.user
    return render(request, 'authenticate/user_account.html', {'user': user})


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        try:
            user.delete()
            messages.success(request, "Your account has been deleted.")
            return redirect('home')
        except Exception as e:
            logger.error("Error occurred during account deletion: %s", str(e))
            messages.error(request, "An error occurred during account deletion. Please try again later.")
            return redirect('view_user')
    else:
        return render(request, 'authenticate/delete_account.html')


def password_change_done(request):
    return render(request, 'authenticate/password_change_done.html')
