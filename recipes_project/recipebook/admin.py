from django.contrib import admin
from .models import Meal, Ingredient


class ChefPage(admin.AdminSite):
    site_header = "Страница шеф повара"


chef_page = ChefPage(name="ChefPage")

chef_page.register(Meal)
chef_page.register(Ingredient)
