from django.shortcuts import render,redirect
from .models import Hotel, UserManager,User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def gallerie(request):
    return render(request,'gallerie.html')
def propos(request):
    return render(request,'propos.html')
def hotel_reservation(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotel_reservation.html', context)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

