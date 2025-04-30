from django.http import HttpResponse
from django.shortcuts import render, redirect
from appone.forms import Form_one, UploadForm, Userform
from .models import contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'appone/index.html')

@login_required
def contactsview(request):
    contacts = contact.objects.filter(currentuser=request.user)
    return render(request, 'appone/home.html', context={"contacts": contacts})

def register(request):
    register = False
    if request.method == "POST":
        userform = Userform(data=request.POST)
        uploadform = UploadForm(data=request.POST)

        if userform.is_valid() and uploadform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = uploadform.save(commit=False)
            profile.user = user

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']
            profile.save()
            register = True
        else:
            print(userform.errors, uploadform.errors)

    else:
        userform = Userform()
        uploadform = UploadForm()

    return render(request, "appone/register.html", context={"userform": userform, "profileform": uploadform, "registered": register})

@login_required
def userlogout(request):
    logout(request)
    return redirect("appone:index")

@login_required
def special(request):
    return render(request, "appone/special.html")

@login_required
def formview(request):
    form = Form_one(request.POST or None)
    if request.method == "POST" and form.is_valid():
        contact_instance = form.save(commit=False)
        contact_instance.currentuser = request.user
        contact_instance.save()
        return redirect("appone:contactsurl")
    return render(request, "appone/forms.html", context={"form": form})

@login_required
def deleteall(request):
    contact.objects.filter(currentuser=request.user).delete()
    return redirect('appone:contactsurl')

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('appone:index')
        else:
            print("Invalid credentials or user is inactive")
    return render(request, 'appone/login.html')
