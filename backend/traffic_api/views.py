from django.http import JsonResponse
from rest_framework.decorators import api_view
import googlemaps
import os

# Google Maps API Client
gmaps = googlemaps.Client(key="AIzaSyDUIkhw9YAxbVIh3cNJQnU99JOGM4OPwno")

@api_view(["GET"])
def traffic_data(request):
    origin = request.GET.get("origin", "28.6139,77.2090")
    destination = request.GET.get("destination", "28.5355,77.3910")

    # Get Directions with Traffic Data
    directions = gmaps.directions(
        origin,
        destination,
        departure_time="now",
        traffic_model="best_guess"
    )

    return JsonResponse(directions, safe=False)
