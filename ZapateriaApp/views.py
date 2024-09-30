from django.shortcuts import render
from .models import calzado_collection
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId

@csrf_exempt
def add_calzado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "nombre": data.get("nombre"),
                "codigoBarras": data.get("codigoBarras"),
                "proveedores": data.get("proveedores"),
                "inversionistas": data.get("inversionistas"),
                "cantidad": data.get("cantidad"),
                "precioCompra": data.get("precioCompra"),
                "precioVenta": data.get("precioVenta"),
                "estado": data.get("estado"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()   
            }
            result = calzado_collection.insert_one(record)
            new_record = calzado_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New calzado added",
                "calzado": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_calzado(request):
    calzados = calzado_collection.find()
    calzados_list = []
    for calzado in calzados:
        calzado['_id'] = str(calzado['_id'])
        calzados_list.append(calzado)
    return JsonResponse(calzados_list, safe=False)

def get_calzado(request, calzado_id):
    try:
        calzado = calzado_collection.find_one({"_id": ObjectId(calzado_id)})
        if calzado:
            calzado['_id'] = str(calzado['_id'])
            return JsonResponse(calzado, safe=False)
        else:
            return JsonResponse({"error": "Calzado not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_calzado(request, calzado_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "nombre": data.get("nombre"),
                "codigoBarras": data.get("codigoBarras"),
                "proveedores": data.get("proveedores"),
                "inversionistas": data.get("inversionistas"),
                "cantidad": data.get("cantidad"),
                "precioCompra": data.get("precioCompra"),
                "precioVenta": data.get("precioVenta"),
                "estado": data.get("estado"),
                "fechaUpdate": datetime.now().isoformat()
            }
            result = calzado_collection.update_one(
                {"_id": ObjectId(calzado_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "Calzado updated"}, status=200)
            else:
                return JsonResponse({"error": "Calzado not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_calzado(request, calzado_id):
    if request.method == 'DELETE':
        try:
            result = calzado_collection.delete_one({"_id": ObjectId(calzado_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "Calzado deleted"}, status=200)
            else:
                return JsonResponse({"error": "Calzado not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
