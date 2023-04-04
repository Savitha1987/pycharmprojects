from os import name

from django.http import HttpResponse
from django.shortcuts import render
from .models import place, star


# Create your views here.
def demo (request):
    obj=place.objects.all()
    sobj = star.objects.all()
    return  render(request,"index.html",{'result':obj,'sresult':sobj})





