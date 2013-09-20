from django.shortcuts import render
from inventory.models import *
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    inventory = Item.objects.all()
    context = { 'inventory_items': inventory}
    return render(request, 'inventory/index.html', context)

def update_inventory(request):
    item = Item.objects.get(upc=request.POST['upc'])

    if 'price' in request.POST:
        item.price = request.POST['price']
    if 'name' in request.POST:
        item.name = request.POST['name']
    if 'scalable' in request.POST:
        if request.POST['scalable'] == 'true':
            item.scalable = true
        else:
            item.scalable = false
    if 'taxable' in request.POST:
        if request.POST['taxable'] == 'true':
            item.taxable = True
        else:
            item.taxable = False
    if 'vendor' in request.POST:
        item.vendor = request.POST['vendor']
    item.save()

    context_instance = { 'item': item }

    return render(request, 'inventory/update_inventory.json', context_instance, content_type="application/json")
