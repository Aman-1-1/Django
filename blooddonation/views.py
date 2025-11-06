from django.shortcuts import render, redirect
from .models import logindoner
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password



def home (request):
    return render (request,'home.html')
def finddoner (request):
    return render (request,'finddoner.html')

def signupdoner_view (request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        blood_type = request.POST.get("blood_type")
        is_donor = True if request.POST.get("is_donor") == "on" else False
        
        # if len(username)<=8 or len(username)>=16:
        #     messages.error(request, "username Should be between 8 to 16 character long")
        #     return render(request, "signup.html")
        
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return render(request, "signup.html")

        if not all([first_name, last_name, email, username, password1, password2]):
            messages.error(request, "Please fill all required fields!")
            return render(request, "signup.html")
        
       

        hashed_password = make_password(password1)

        logindoner.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=hashed_password,
            blood_type=blood_type,
            is_donor=is_donor
        )

        messages.success(request, "Signup successful! You can now log in.")
        return redirect("login")

    return render(request, "signup.html")

def logindoner_view(request):
    if request.session.get("user_id"):
        return redirect ("home")
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        user = logindoner.objects.filter(username=username_or_email).first() or \
                    logindoner.objects.filter(email=username_or_email).first()

        if user and check_password(password, user.password):
            request.session["user_id"] = user.id
            request.session["username"] = user.username
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect('login')


# Create your views here.

