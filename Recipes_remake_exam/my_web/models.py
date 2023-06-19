from django.db import models


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENTS_MAX_LEN = 250

    title = models.CharField(
        max_length=TITLE_MAX_LEN,

    )

    image_url = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LEN,
    )

    time = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title},id={self.pk}'
