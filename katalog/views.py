from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_katalog_item,
        'name': 'Kaloosh Falito Verrell',
        'npm': '2106720916'
    }
    return render(request, "katalog.html", context)