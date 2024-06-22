from django.shortcuts import render, redirect
from .models import Event
from .forms import RegisterForm
from .models import Register


# Create your views here.
def dashboard(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            register = form.save(commit=False)
            # Generate registration number
            register.generate_registration_number()
            register.save()
            return render(request, 'registration_success.html', {'register': register})
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
