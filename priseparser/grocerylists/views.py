from django.shortcuts import render
from .models import GroceryLists


def lists_home(request):
    grocerylists = GroceryLists.objects.order_by('red_date')
    return render(request, 'grocerylists/lists_home.html', {'grocerylists': grocerylists})
