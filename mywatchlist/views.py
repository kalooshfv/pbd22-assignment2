from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import time

# Create your views here.
def show_watchlist(request):
    data_watchlist_item = WatchlistItem.objects.all()
    watched = 0
    not_watched = 0
    for movie in data_watchlist_item:
        if movie.item_watched == "Yes":
            watched += 1
        elif movie.item_watched == "No":
            not_watched += 1
    if watched >= not_watched and watched > 0:
        report = "Congratulations, you have watched a lot of movies!"
    else:
        report = "Woah, you need to watch more movies!"
    context = {
        'list_item': data_watchlist_item,
        'name': 'Kaloosh Falito Verrell',
        'npm': '2106720916',
        'report': report
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), \
        content_type="application/xml")

@csrf_exempt
def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), \
        content_type="application/xml")

def show_json_by_id(request, id):
    data = WatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), \
        content_type="application/json")


