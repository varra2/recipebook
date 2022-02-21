from django.shortcuts import render
from recipebook.models import Meal, Ingredient


def index(request):

    if request.method == "GET":
        recipes = Meal.objects.all()
    elif request.method == "POST":
        if "lookup_recipe" in request.POST and "lookup_ingredient" in request.POST:
            lookup_recipe = request.POST["lookup_recipe"].lower()
            lookup_ingredient = request.POST["lookup_ingredient"]
            meal = set(Meal.objects.filter(name__icontains=lookup_recipe))
            ingredient = set(Meal.objects.filter(ingredients__in=[lookup_ingredient]))
            recipes = meal.intersection(ingredient)
        elif "lookup_ingredient" in request.POST:
            lookup_ingredient = request.POST["lookup_ingredient"]
            recipes = Meal.objects.filter(ingredients__in=[lookup_ingredient])
        elif "lookup_recipe" in request.POST:
            lookup_recipe = request.POST["lookup_recipe"]
            recipes = Meal.objects.filter(name__icontains=lookup_recipe)
    ingredients = Ingredient.objects.all()
    return render(
        request,
        "recipebook/index.html",
        {"recipes": recipes, "ingredients": ingredients},
    )
