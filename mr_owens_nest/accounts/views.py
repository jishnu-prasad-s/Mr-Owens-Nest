from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm

@user_passes_test(lambda u: u.is_superuser)
def RegisterView(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            return redirect(reverse('auth:login'))
    else:
        form = UserForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'accounts/register.html', context=context)

def LoginView(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
    #     print(form)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, email=email, password=password)
            print(email, password, user)
            if user is not None:
                login(request, user=user)
                return redirect('inventory:list')
    else:
        form = AuthenticationForm(request)
    return render(request, "accounts/login.html", context={"form":form})

def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect(reverse('home'))
    return render(request, "accounts/logout.html", {})
