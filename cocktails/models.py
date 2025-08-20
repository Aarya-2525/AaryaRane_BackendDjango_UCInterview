from django.db import models

# Create your models here.
class CocktailSearch(models.Model):
    name = models.CharField(max_length=200, unique=True)  # cocktail name
    count = models.PositiveIntegerField(default=0)        # how many times searched

    def __str__(self):
        return f"{self.name} ({self.count})"