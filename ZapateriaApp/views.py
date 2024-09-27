from django.shortcuts import render
from .models import calzado_collection
from django.http import HttpResponse

# Create your views here.
def index(requet):
    return HttpResponse("<h1>Hola</h1>")

def add_person(request):
    records={
        ""
    }