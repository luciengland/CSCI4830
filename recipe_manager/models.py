from django.db import models

# create recipe model
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    cuisine = models.CharField(max_length=100, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    time_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
