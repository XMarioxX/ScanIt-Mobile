from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  

inversionista_collection = db['Inversionista']  

@csrf_exempt
def add_inversionista(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "nombre": data.get("nombre"),
                "presupuesto": data.get("presupuesto"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()  
            }
            result = inversionista_collection.insert_one(record)  
            new_record = inversionista_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New inversionista added",
                "inversionista": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_inversionista(request):
    inversionistas = inversionista_collection.find()
    inversionistas_list = []
    for inversionista in inversionistas:
        inversionista['_id'] = str(inversionista['_id'])
        inversionistas_list.append(inversionista)
    return JsonResponse(inversionistas_list, safe=False)

def get_inversionista(request, inversionista_id):
    try:
        inversionista = inversionista_collection.find_one({"_id": ObjectId(inversionista_id)})
        if inversionista:
            inversionista['_id'] = str(inversionista['_id'])
            return JsonResponse(inversionista, safe=False)
        else:
            return JsonResponse({"error": "Inversionista not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_inversionista(request, inversionista_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "nombre": data.get("nombre"),
                "presupuesto": data.get("presupuesto"),
                "fechaUpdate": datetime.now().isoformat() 
            }
            result = inversionista_collection.update_one(
                {"_id": ObjectId(inversionista_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "Inversionista updated"}, status=200)
            else:
                return JsonResponse({"error": "Inversionista not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_inversionista(request, inversionista_id):
    if request.method == 'DELETE':
        try:
            result = inversionista_collection.delete_one({"_id": ObjectId(inversionista_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "Inversionista deleted"}, status=200)
            else:
                return JsonResponse({"error": "Inversionista not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
