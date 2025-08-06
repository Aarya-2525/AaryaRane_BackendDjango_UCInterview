import requests
from django.shortcuts import render

def cocktails_search(request):
    query = request.GET.get("query")
    results = None

    if query:
        url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}"
        response = requests.get(url)
        data = response.json()
        results = data.get("drinks")

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)

def cocktail_detail(request, cocktail_id):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}"
    response = requests.get(url)
    data = response.json()
    drink = data.get("drinks")[0] if data.get("drinks") else None

    # Extract first 3 ingredients + measures
    ingredients = []
    for i in range(1, 4):  # first 3 ingredients
        ing = drink.get(f"strIngredient{i}")
        meas = drink.get(f"strMeasure{i}")
        if ing:
            ingredients.append((ing, meas))

    context = {
        "drink": drink,
        "ingredients": ingredients,
    }
    return render(request, "details.html", context)