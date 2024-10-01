from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from bson import ObjectId
from db_connection import db  
import bcrypt

usuario_collection = db['Usuario']  

@csrf_exempt
def add_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            password_plain = data.get("password")
            hashed_password = bcrypt.hashpw(password_plain.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            record = {
                "nombre": data.get("nombre"),
                "email": data.get("email"),
                "password": hashed_password,
                "telefono": data.get("telefono"),
                "cantidad": data.get("cantidad"),
                "fechaCreate": datetime.now().isoformat(),  
                "fechaUpdate": datetime.now().isoformat()  
            }
            result = usuario_collection.insert_one(record)  
            new_record = usuario_collection.find_one({"_id": result.inserted_id})
            new_record["_id"] = str(new_record["_id"])
            response_data = {
                "message": "New usuario added",
                "usuario": new_record
            }
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_usuario(request):
    usuarios = usuario_collection.find()
    usuarios_list = []
    for usuario in usuarios:
        usuario['_id'] = str(usuario['_id'])
        usuarios_list.append(usuario)
    return JsonResponse(usuarios_list, safe=False)

def get_usuario(request, usuario_id):
    try:
        usuario = usuario_collection.find_one({"_id": ObjectId(usuario_id)})
        if usuario:
            usuario['_id'] = str(usuario['_id'])
            return JsonResponse(usuario, safe=False)
        else:
            return JsonResponse({"error": "Usuario not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_usuario(request, usuario_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            updated_data = {
                "nombre": data.get("nombre"),
                "email": data.get("email"),
                "password": data.get("password"),
                "telefono": data.get("telefono"),
                "cantidad": data.get("cantidad"),
                "fechaUpdate": datetime.now().isoformat() 
            }
            result = usuario_collection.update_one(
                {"_id": ObjectId(usuario_id)}, {"$set": updated_data}
            )
            if result.matched_count > 0:
                return JsonResponse({"message": "Usuario updated"}, status=200)
            else:
                return JsonResponse({"error": "Usuario not found"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def delete_usuario(request, usuario_id):
    if request.method == 'DELETE':
        try:
            result = usuario_collection.delete_one({"_id": ObjectId(usuario_id)})
            if result.deleted_count > 0:
                return JsonResponse({"message": "Usuario deleted"}, status=200)
            else:
                return JsonResponse({"error": "Usuario not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)
