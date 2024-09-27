from django.shortcuts import render
from .models import calzado_collection
from django.http import HttpResponse

# Create your views here.
def index(requet):
    return HttpResponse("<h1>Hola</h1>")

def add_calzado(request):
    records={
        "first_name":"Mario",
        "last_name":"Sanchez"
    }
    calzado_collection.insert_one(records)
    return HttpResponse("New person is added")

def get_all_calzado(request):
    calzados=calzado_collection.find()
    return HttpResponse(calzados)