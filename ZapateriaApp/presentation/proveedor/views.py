from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  

proveedor_collection = db['Proveeodr']  

@csrf_exempt
def add_proveedor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "nombre": data.get("nombre"),
                "telefono": data.get("telefono"),
                "direccion": data.get("direccion"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat(),
                "tipo": data.get("tipo")  
            }
            result = proveedor_collection.insert_one(record)  
            new_record = proveedor_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New proveedor added",
                "proveedor": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_proveedor(request):
    proveedores = proveedor_collection.find()
    proveedores_list = []
    for proveedor in proveedores:
        proveedor['_id'] = str(proveedor['_id'])
        proveedores_list.append(proveedor)
    return JsonResponse(proveedores_list, safe=False)

def get_provedor(request, proveedor_id):
    try:
        proveedor = proveedor_collection.find_one({"_id": ObjectId(proveedor_id)})
        if proveedor:
            proveedor['_id'] = str(proveedor['_id'])
            return JsonResponse(proveedor, safe=False)
        else:
            return JsonResponse({"error": "Proveedor not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_proveedor(request, proveedor_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "nombre": data.get("nombre"),
                "telefono": data.get("telefono"),
                "direccion": data.get("direccion"),
                "fechaUpdate": datetime.now().isoformat(),
                "tipo": data.get("tipo"),
            }
            result = proveedor_collection.update_one(
                {"_id": ObjectId(proveedor_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "Proveedor updated"}, status=200)
            else:
                return JsonResponse({"error": "Proveedor not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_proveedor(request, proveedor_id):
    if request.method == 'DELETE':
        try:
            result = proveedor_collection.delete_one({"_id": ObjectId(proveedor_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "Proveedor deleted"}, status=200)
            else:
                return JsonResponse({"error": "Proveedor not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
