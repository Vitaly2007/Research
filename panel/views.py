from django import template
from django.shortcuts import render

from panel.models import Subsidiary, Station

def index(request):
    subsidiarys = Subsidiary.objects.all()
    context = {'subsidiarys':subsidiarys}
    return render(request, 'panel/index.html', context)

def by_station(request, subsidiary_id):
    subsidiary = Subsidiary.objects.get(pk=subsidiary_id)
    stations = Station.objects.filter(subsidiary=subsidiary_id)
    context = {'stations':stations, 'subsidiary':subsidiary}
    return render(request, 'panel/by_station.html', context)