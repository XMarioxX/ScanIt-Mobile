from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  

calzadoTalla_collection = db['CalzadoTalla']  

@csrf_exempt
def add_calzadoTalla(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            record = {
                "valueMX": data.get("valueMX"),
                "valueCN": data.get("valueCN"),
                "valueUS": data.get("valueUS"),
                "valueEU": data.get("valueEU"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()  
            }
            result = calzadoTalla_collection.insert_one(record)  
            new_record = calzadoTalla_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New calzadoTalla added",
                "calzadoTalla": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_calzadoTalla(request):
    calzadoTallas = calzadoTalla_collection.find()
    calzadoTallas_list = []
    for calzadoTalla in calzadoTallas:
        calzadoTalla['_id'] = str(calzadoTalla['_id'])
        calzadoTallas_list.append(calzadoTalla)
    return JsonResponse(calzadoTallas_list, safe=False)

def get_calzadoTalla(request, calzadoTalla_id):
    try:
        calzadoTalla = calzadoTalla_collection.find_one({"_id": ObjectId(calzadoTalla_id)})
        if calzadoTalla:
            calzadoTalla['_id'] = str(calzadoTalla['_id'])
            return JsonResponse(calzadoTalla, safe=False)
        else:
            return JsonResponse({"error": "CalzadoTalla not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_calzadoTalla(request, calzadoTalla_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "valueMX": data.get("valueMX"),
                "valueCN": data.get("valueCN"),
                "valueUS": data.get("valueUS"),
                "valueEU": data.get("valueEU"),
                "fechaUpdate": datetime.now().isoformat() 
            }
            result = calzadoTalla_collection.update_one(
                {"_id": ObjectId(calzadoTalla_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "CalzadoTalla updated"}, status=200)
            else:
                return JsonResponse({"error": "CalzadoTalla not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_calzadoTalla(request, calzadoTalla_id):
    if request.method == 'DELETE':
        try:
            result = calzadoTalla_collection.delete_one({"_id": ObjectId(calzadoTalla_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "CalzadoTalla deleted"}, status=200)
            else:
                return JsonResponse({"error": "CalzadoTalla not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
