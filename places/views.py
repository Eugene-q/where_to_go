from django.shortcuts import get_object_or_404, render
from .models import Location, Image
from geojson import FeatureCollection
from django.http import JsonResponse

def map_view(request):
    features = [location.get_feature() for location in Location.objects.all()]
    context = {
        'locations' : FeatureCollection(features)
    }
    return render(request, 'map.html', context)

def location_view(request, id):
    location = get_object_or_404(Location, id=id)
    response_data = {
        'title' : location.title,
        'imgs' : [image.image.url for image in location.images.all()],
        'short_description' : location.short_description,
        'long_description' : location.long_description,
        'coordinates' : {
            'lng' : location.lng_coordinate,
            'lat' : location.lat_coordinate,
        }
    }
    response_params = {
        'ensure_ascii' : False,
        'indent' : 4,
    }
    return JsonResponse(response_data, json_dumps_params=response_params)