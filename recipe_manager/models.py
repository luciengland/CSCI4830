from django.db import models

# create recipe model
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    cuisine = models.CharField(max_length=100, blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    time_commitment = models.CharField(
        max_length=10,
        choices=[
            ('Quick', 'Quick'),
            ('Average', 'Average'),
            ('Long', 'Long'),
        ],
        default='Average'
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
