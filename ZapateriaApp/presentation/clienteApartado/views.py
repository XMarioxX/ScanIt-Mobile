from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  

clienteApartado_collection = db['ClienteApartado']  

@csrf_exempt
def add_clienteApartado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "nombre": data.get("nombre"),
                "telefono": data.get("telefono"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()  
            }
            result = clienteApartado_collection.insert_one(record)  
            new_record = clienteApartado_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New clienteApartado added",
                "clienteApartado": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_clienteApartado(request):
    clienteApartados = clienteApartado_collection.find()
    clienteApartados_list = []
    for clienteApartado in clienteApartados:
        clienteApartado['_id'] = str(clienteApartado['_id'])
        clienteApartados_list.append(clienteApartado)
    return JsonResponse(clienteApartados_list, safe=False)

def get_clienteApartado(request, clienteApartado_id):
    try:
        clienteApartado = clienteApartado_collection.find_one({"_id": ObjectId(clienteApartado_id)})
        if clienteApartado:
            clienteApartado['_id'] = str(clienteApartado['_id'])
            return JsonResponse(clienteApartado, safe=False)
        else:
            return JsonResponse({"error": "ClienteApartado not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_clienteApartado(request, clienteApartado_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "nombre": data.get("nombre"),
                "telefono": data.get("telefono"),
                "fechaUpdate": datetime.now().isoformat() 
            }
            result = clienteApartado_collection.update_one(
                {"_id": ObjectId(clienteApartado_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "ClienteApartado updated"}, status=200)
            else:
                return JsonResponse({"error": "ClienteApartado not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_clienteApartado(request, clienteApartado_id):
    if request.method == 'DELETE':
        try:
            result = clienteApartado_collection.delete_one({"_id": ObjectId(clienteApartado_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "ClienteApartado deleted"}, status=200)
            else:
                return JsonResponse({"error": "ClienteApartado not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
