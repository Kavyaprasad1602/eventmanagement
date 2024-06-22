from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return redirect('register/')  # Change the redirect URL to 'signin' without trailing slash
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken")
                return redirect('register/')  # Change the redirect URL to 'signin' without trailing slash
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.success(request, "Account created successfully")
                return redirect('home')  # Change the redirect URL to 'signin' without trailing slash
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register/')  # Redirect back to signup page if passwords don't match

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successfully")
            return redirect('home')
        else:
            messages.success(request, "invalid")
            return redirect('register/')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
