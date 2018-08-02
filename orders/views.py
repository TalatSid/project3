from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

#, Item_ctg, Orders, Deliv_meth, Diet_pref

# Create your views here.
def index(request):
   context = {
        "orders": Item.objects.all()
   }
   return render(request, "orders/index.html", context)
