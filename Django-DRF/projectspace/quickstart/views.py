from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from quickstart.models import Item
from quickstart.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
# Create your views here.

@api_view(['GET'])
def getdata(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getby_id(request,pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['GET'])
def get_by_place(request,place):
    item = Item.objects.filter(place=place)
    serializer = ItemSerializer(item,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    r = request.data.get('place') 
    if not isinstance(r,str):
        return Response({"message":"must be a string"},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ItemSerializer(data = request.data)

    #handle string validation above 
    #request.data is the data that was sent from the front end
   
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_item(request,pk):
    item = Item.objects.get(id = pk)
    serializer = ItemSerializer(item,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_item(request,pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response({"message":"item deleted Sucessfully"})


    