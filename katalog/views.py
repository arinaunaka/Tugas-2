from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_katalog,
    'nama': 'Arina Aunaka',
    'npm': '2106638690',
}
    return render(request, "katalog.html", context)