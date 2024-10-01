from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  

calzadoEstado_collection = db['CalzadoEstado']  

@csrf_exempt
def add_calzadoEstado(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "active": data.get("active"),
                "inactive": data.get("inactive"),
                "deleted": data.get("deleted"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()  
            }
            result = calzadoEstado_collection.insert_one(record)  
            new_record = calzadoEstado_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New calzadoEstado added",
                "calzadoEstado": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_calzadoEstado(request):
    calzadoEstados = calzadoEstado_collection.find()
    calzadoEstados_list = []
    for calzadoEstado in calzadoEstados:
        calzadoEstado['_id'] = str(calzadoEstado['_id'])
        calzadoEstados_list.append(calzadoEstado)
    return JsonResponse(calzadoEstados_list, safe=False)

def get_calzadoEstado(request, calzadoEstado_id):
    try:
        calzadoEstado = calzadoEstado_collection.find_one({"_id": ObjectId(calzadoEstado_id)})
        if calzadoEstado:
            calzadoEstado['_id'] = str(calzadoEstado['_id'])
            return JsonResponse(calzadoEstado, safe=False)
        else:
            return JsonResponse({"error": "CalzadoEstado not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_calzadoEstado(request, calzadoEstado_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "active": data.get("active"),
                "inactive": data.get("inactive"),
                "deleted": data.get("deleted"),
                "fechaUpdate": datetime.now().isoformat() 
            }
            result = calzadoEstado_collection.update_one(
                {"_id": ObjectId(calzadoEstado_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "CalzadoEstado updated"}, status=200)
            else:
                return JsonResponse({"error": "CalzadoEstado not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_calzadoEstado(request, calzadoEstado_id):
    if request.method == 'DELETE':
        try:
            result = calzadoEstado_collection.delete_one({"_id": ObjectId(calzadoEstado_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "CalzadoEstado deleted"}, status=200)
            else:
                return JsonResponse({"error": "CalzadoEstado not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
