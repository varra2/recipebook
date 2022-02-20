from django.shortcuts import render
from recipebook.models import Meal, Ingredient


def index(request):

    if request.method == "GET":
        recipes = Meal.objects.all()
    if request.method == "POST":
        lookup_recipe = request.POST["lookup_recipe"].lower()
        print(lookup_recipe)
        recipes = Meal.objects.filter(name__icontains=lookup_recipe)

    return render(request, "recipebook/index.html", {"recipes": recipes})
