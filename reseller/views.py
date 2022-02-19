from django.shortcuts import render

# Create your views here.
def resellerboard(request):
    return render(request, "reseller/dashboard.html")

