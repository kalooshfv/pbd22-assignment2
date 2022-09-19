from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist_item = WatchlistItem.objects.all()
    context = {
        'list_item': data_watchlist_item,
        'name': 'Kaloosh Falito Verrell',
        'npm': '2106720916'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), \
        content_type="application/xml")

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



