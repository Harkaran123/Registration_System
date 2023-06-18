from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Login_Page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Haa bhaii galat password ya username hai tumharra...bhosdikkkeee")
        
    return render(request, 'login.html')

def Signup_Page(request):

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Password and Confirm_Pssword are not same")
        my_user = User.objects.create_user(uname, email, password1)
        my_user.save()

        return redirect('login')
    
    return render(request, 'signup.html')

@login_required(login_url="login")
def Home_Page(request):
    return render(request, 'home.html')

def Logout_Page(request):
    logout(request)
    return redirect('login')

# Create your views here.
