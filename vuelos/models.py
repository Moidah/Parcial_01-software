from django.db import models

class Flight(models.Model):
    NATIONAL = 'Nacional'
    INTERNATIONAL = 'Internacional'
    FLIGHT_TYPE_CHOICES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]
    
    name = models.CharField(max_length=100)
    flight_type = models.CharField(max_length=15, choices=FLIGHT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
