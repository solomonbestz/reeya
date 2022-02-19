from django.shortcuts import render
from authentication.models import Wholseller

# Create your views here.
def wholesalerboard(request):

    return render(request, "wholesaler/dashboard.html")
