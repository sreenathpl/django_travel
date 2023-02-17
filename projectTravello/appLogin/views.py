from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def user_login(request):
    if request.method =="POST":
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username = user_name,
                                 password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"Incorrect username and password")
    return render(request,'user_login.html')

def user_logout(request):
    auth.logout(request)
    return redirect("/")


def user_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return redirect('user_reg')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"EMail already exists")
                return redirect('user_reg')
            else:
                user = User.objects.create_user(username = username,
                                                password = password,
                                                first_name = first_name,
                                                last_name = last_name,
                                                email = email,)
                user.save()
                return redirect('user_login')
        else:
            messages.info(request, "Password not matching")
            return redirect('user_reg')
        return redirect('/')
    return render(request,'user_regg.html')