from django.shortcuts import render, redirect
from .forms import FlightForm
from django.db.models import Avg
from .models import Flight

# Vista para la página de inicio
def home(request):
    return render(request, 'vuelos/home.html')

# Vista para registrar un vuelo
# Esta vista tiene tanto GET como POST para mostrar y procesar el formulario.
def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('list_flights')  
    else:
        form = FlightForm()
    return render(request, 'vuelos/register_flight.html', {'form': form})

# Vista para listar todos los vuelos
def list_flights(request):
    flights = Flight.objects.all().order_by('price')  # Obtiene los vuelos de la base de datos y los ordena por precio
    return render(request, 'vuelos/list_flights.html', {'flights': flights})

# Vista para mostrar las estadísticas de vuelos
def flight_statistics(request):
    total_national = Flight.objects.filter(flight_type='Nacional').count() # cuenta cuantos nacionales hay
    total_international = Flight.objects.filter(flight_type='Internacional').count() #cuenta cuantos inter hay
    avg_national_price = Flight.objects.filter(flight_type='Nacional').aggregate(Avg('price'))['price__avg'] or 0  #calcula el precio
    return render(request, 'vuelos/flight_statistics.html', {
        'total_national': total_national,
        'total_international': total_international,
        'avg_national_price': avg_national_price,
    })
