from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def sucursales(request):
    sucursales = Proyecto.objects.all()
    return render(request, "sucursales/sucursales.html", {'sucursales':sucursales})