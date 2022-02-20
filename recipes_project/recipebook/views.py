from django.shortcuts import render
from recipebook.models import Meal, Ingredient


def index(request):

    recipes = Meal.objects.all()

    return render(request, "recipebook/index.html", {"recipes": recipes})
