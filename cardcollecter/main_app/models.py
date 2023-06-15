from django.db import models
from django.urls import reverse


MARKET = (
    ('B', 'BGS'),
    ('P', 'PSA'),
    ('C', 'CGC'),
)

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    grade = models.IntegerField()


# Changing this instance Method does not impact the database
# therefore no makemigrations is needed 


    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})



class Market(models.Model):
    date  = models.DateField()
    price = models.CharField(
        max_length=1,
        choices =MARKET,
        default=MARKET [0][0]
)
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
)

    def __str__(self):
        return f"{self.get_price_display()} on {self.date}"