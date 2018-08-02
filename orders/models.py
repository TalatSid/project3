from django.db import models

# Create your models here.
class Item(models.Model):
    item = models.CharField(max_length = 64)
    cost = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        return f"{self.item} ({self.cost})"
