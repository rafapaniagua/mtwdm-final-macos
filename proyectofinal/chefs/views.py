from django.shortcuts import render

# Create your views here.
def chefs(request):
    return render(request, "chefs/chefs.html")