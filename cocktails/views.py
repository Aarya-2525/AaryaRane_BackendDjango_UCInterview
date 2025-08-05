from django.shortcuts import render
import requests

def cocktails_search(request):
    query = request.GET.get("query")
    results = None

    if query:
        ingredients = [i.strip() for i in query.split(",")]
        drink_sets = []

        for ingredient in ingredients:
            url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}"
            response = requests.get(url)
            data = response.json()
            drinks = data.get("drinks", [])
            ids = {drink["idDrink"]: drink for drink in drinks if drinks}
            drink_sets.append(ids)

        if drink_sets:
            common_ids = set(drink_sets[0].keys())
            for drink_dict in drink_sets[1:]:
                common_ids &= set(drink_dict.keys())

            results = [drink_sets[0][id] for id in common_ids]
        else:
            results = []


    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)
