from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import convert

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def api(request, lat, long):
    data = convert.get_sun_coords(lat, long)
    return JsonResponse(data)

def api_date(request, lat, long, date):
    data = convert.get_sun_coords(lat, long, date)
    return JsonResponse(data)
