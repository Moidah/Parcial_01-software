from django.shortcuts import render, redirect
from .forms import FlightForm
from django.db.models import Avg
from .models import Flight

def home(request):
    return render(request, 'vuelos/home.html')

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('list_flights')  
    else:
        form = FlightForm()
    return render(request, 'vuelos/register_flight.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'vuelos/list_flights.html', {'flights': flights})

def flight_statistics(request):
    total_national = Flight.objects.filter(flight_type='Nacional').count()
    total_international = Flight.objects.filter(flight_type='Internacional').count()
    avg_national_price = Flight.objects.filter(flight_type='Nacional').aggregate(Avg('price'))['price__avg'] or 0
    return render(request, 'vuelos/flight_statistics.html', {
        'total_national': total_national,
        'total_international': total_international,
        'avg_national_price': avg_national_price,
    })
