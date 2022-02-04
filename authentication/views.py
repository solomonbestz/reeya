from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

update_username = ''

# Authentication Home View.
def home(request):
    return render(request, "authentication/index.html")

# Authentication Signup choice to ask if the clients wants to be a wholesaler or reseller.
def signupchoice(request):
    return render(request, "authentication/signupchoice.html")

# Authentication for wholesaler signup
def signupwholsaler(request):
    global update_username
    if request.method == 'POST':
        company_name = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        username = first_name +" "+ last_name
        update_username = username
        my_user = User.objects.create_user(username, email, password1)
        my_user.first_name = first_name
        my_user.last_name = last_name

        my_user.save()

        messages.success(request, "Your Account Has Been Successfully Created.")
        return redirect('signin')

    return render(request, "authentication/signupwholesaler.html")


# Authentication for reseller sign up
def signupreseller(request):
    if request.method == 'POST':
        pass
    return render(request, "authentication/signupreseller.html")

    
# Authenticatin Signin View
def signin(request):
    if request.method == 'POST':
        user1 = request.POST.get('username')
        pass1 = request.POST.get('password')

        user =  authenticate(username=user1, password=pass1)

        if user is not None:
            login(request, user)
            first_name = user.username
            return render(request, "wholesaler/dashboard.html", {'fname':first_name})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')


    return render(request, "authentication/signin.html", {'username':update_username})

# Authentication Signout View
def signout(request):
    pass