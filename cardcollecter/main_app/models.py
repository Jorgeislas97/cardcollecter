from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    grade = models.IntegerField()


# Changing this instance Method does not impact the database
# therefore no makemigrations is needed 


def __str__(self):
    return self.name