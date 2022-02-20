from tabnanny import verbose
from django.db import models


class Meal(models.Model):
    name = models.CharField("Название", max_length=150)
    recipe = models.TextField("Рецепт")
    ingridients = models.ManyToManyField(
        "Ingridient", verbose_name="Ингридиенты", related_name="meals"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Ingridient(models.Model):
    name = models.CharField("Название ингридиента", max_length=150)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"
