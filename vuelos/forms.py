from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'flight_type', 'price']
        widgets = {
            'flight_type': forms.Select(choices=Flight.FLIGHT_TYPE_CHOICES),
        }
