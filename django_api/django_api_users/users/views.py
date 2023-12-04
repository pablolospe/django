from django.shortcuts import render

# Create your views here.
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for user
from .serializers import UserSerializer
# User model
from .models import User


# Manejo de solicitudes entrantes para obtener y crear usuarios
@csrf_exempt
def users(request):
    '''
    List all user snippets
    '''
    if(request.method == 'GET'):
        # get all the users
        users = User.objects.all()
        # serialize the user data
        serializer = UserSerializer(users, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    
# Manejo de solicitudes entrantes para actualizar y eliminar usuarios
@csrf_exempt
def user_detail(request, pk):
    try:
        # obtain the user with the passed id.
        user = User.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = UserSerializer(user, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = UserSerializer(user, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the user
        user.delete() 
        # return a no content response.
        return HttpResponse(status=204)