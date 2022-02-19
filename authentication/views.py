from django.shortcuts import render, redirect

from .models import Wholseller, Reseller
from django.contrib import messages
from .reeyafunc import check_password


# Authentication Home View.
def home(request):
    return render(request, "authentication/index.html")

# Authentication Signup choice to ask if the clients wants to be a wholesaler or reseller.
def signupchoice(request):
    return render(request, "authentication/signupchoice.html")

# Authentication for login choice
def loginchoice(request):
    wholesalers = Wholseller.objects.all()
    resellers = Reseller.objects.all()
    return render(request, "authentication/loginchoice.html", {'wholesaler': wholesalers})


# Authentication for wholesaler signup
def signupwholsaler(request):
    if request.method == 'POST':
        company_name = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        check = check_password(password1, password2)

        if check:
            username = first_name +" "+ last_name
            wholesaler_user = Wholseller.objects.create(company_name=company_name, first_name=first_name, last_name=last_name, email=email, password=password1)
            wholesaler_user.save()
            messages.success(request, username+ " Your Account Has Been Successfully Created.")
            return redirect('home')
        else:
            messages.error(request, "Passwords don't match")

    return render(request, "authentication/signupwholesaler.html")


# Authentication for reseller sign up
def signupreseller(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        check = check_password(password1, password2)

        if check:
            username = first_name +" "+ last_name
            reseller_user = Reseller.objects.create(first_name=first_name, last_name=last_name, email=email, password=password1)
            reseller_user.save()
            messages.success(request, username+ " Your Account Has Been Successfully Created.")
            return redirect('home')
        else:
            messages.error(request, "Passwords don't match")
    return render(request, "authentication/signupreseller.html")

    
# Authenticatin Signin View
def loginwholesaler(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            wholeseller_user =  Wholseller.objects.get(email=email, password=password)
            username = wholeseller_user.first_name +" "+ wholeseller_user.last_name
            if email == wholeseller_user.email and password == wholeseller_user.password:
                return redirect("wholesalerboard")
            else:
                messages.error(request, "Bad Credentials")
                return redirect('home')
        except:
             messages.error(request, "Bad Credentials")
             return redirect('loginchoice')
            
    return render(request, "authentication/loginwholesaler.html")

# Authenticatin Signin View
def loginreseller(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            reseller_user =  Reseller.objects.get(email=email, password=password)
            username = reseller_user.first_name +" "+ reseller_user.last_name
            if email == reseller_user.email and password == reseller_user.password:
                return render(request, "reseller/dashboard.html", {'fname':username})
            else:
                messages.error(request, "Bad Credentials")
                return redirect('home')
        except:
             messages.error(request, "Bad Credentials")
             return redirect('loginchoice')
            
    return render(request, "authentication/loginreseller.html")

# Authentication Signout View
def signout(request):
    pass