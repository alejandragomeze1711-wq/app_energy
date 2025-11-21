from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginAuthenticationForm, RegisterForm

# Create your views here.
def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])

        if not user:
            return render(request, "login.html",{
                "form": LoginAuthenticationForm(),
                "error": "Username or password incorrect"
            })
        else:
            login(request, user)
            return redirect("home")
    else:
        if request.user.is_authenticated:
            return redirect("home")
            
        return render(request, "login.html",{
            "form": LoginAuthenticationForm()
        })
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, "errors": form.errors.items() })

def terminate_session(request):
    logout(request)
    return redirect("/auth")