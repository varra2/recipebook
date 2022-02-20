from django.shortcuts import render
from recipebook.models import Meal, Ingredient


def index(request):

    if request.method == "GET":
        recipes = Meal.objects.all()
    if request.method == "POST":
        if "lookup_recipe" in request.POST:
            lookup_recipe = request.POST["lookup_recipe"].lower()
            recipes = Meal.objects.filter(name__icontains=lookup_recipe)
        elif "lookup_ingredient" in request.POST:
            lookup_ingredient = request.POST["lookup_ingredient"]
            recipes = Meal.objects.filter(ingredients__in=[lookup_ingredient])
    ingredients = Ingredient.objects.all()

    return render(
        request,
        "recipebook/index.html",
        {"recipes": recipes, "ingredients": ingredients},
    )
