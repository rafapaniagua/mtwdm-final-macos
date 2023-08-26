from django.shortcuts import render
import requests

# Create your views here.
def bebidadia(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')

    drinks = response.json()
    # print(drinks["drinks"])

    return render(request, "bebidadia/bebidadia.html", {'drink':drinks["drinks"][0]})
    # return render(request, "bebidadia/bebidadia.html")