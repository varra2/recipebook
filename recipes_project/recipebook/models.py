from tabnanny import verbose
from django.db import models


class Meal(models.Model):
    name = models.CharField("Название", max_length=150)
    recipe = models.TextField("Рецепт")
    ingredients = models.ManyToManyField(
        "Ingredient", verbose_name="Ингредиенты", related_name="meals"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Ingredient(models.Model):
    name = models.CharField("Название ингредиента", max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
