from django.shortcuts import render
import requests

def bebidas(request, inicial):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f='+inicial)

    drinks = response.json()
    # print(drinks["drinks"])
    # print(inicial)

    return render(request, "bebidas/bebidas.html", {'drinks':drinks["drinks"]})
    # return render(request, "bebidas/bebidas.html")