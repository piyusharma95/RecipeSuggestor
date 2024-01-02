import requests

from django.shortcuts import render
from django.http import JsonResponse

from django.conf import settings


def get_recipes(request):
    if request.method == "POST":
        ingredients = request.POST.get('ingredients')
        recipes = fetch_recipes(ingredients)
        return render(request, 'recipes.html', {'recipes': recipes})
    return render(request, 'index.html')


def fetch_recipes(ingredients):
    api_key = settings.API_KEY
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()


def ingredient_suggestions(request):
    # This function should return a list of ingredient suggestions
    suggestions = ['Tomato', 'Onion', 'Garlic', 'Carrot', 'Potato', 'Capsicum']
    return JsonResponse(suggestions, safe=False)


# view function to fetch recipe details
def get_recipe_details(request, recipe_id):
    api_key = settings.API_KEY
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
    response = requests.get(url)
    return JsonResponse(response.json())
