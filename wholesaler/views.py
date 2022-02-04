from django.shortcuts import render

# Create your views here.

def wholesalerboard(request):
    return render(request, "wholesaler/dashboard.html")
