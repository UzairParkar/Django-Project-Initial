from django.shortcuts import render
from viewsets.serializers import MobileSerializer
from viewsets.models import Mobile
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

# Create your views here.


# A View Set has default actions for listing, retriving, destroying, updating
# and partial updating, creating

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class  = MobileSerializer


    @action(detail=True,methods=['GET'],url_path='filter-model')
    def filter_model(self,request,pk=None):
        r = Mobile.objects.get(pk=pk)
        print(r)
        serializer = MobileSerializer(r)
        print(serializer.data)
        return Response(serializer.data)

    






































































































































#------------------------------------------------------------------------------------------------------------

# class MobileViewSet(viewsets.ModelViewSet):
#     serializer_class = MobileSerializer
#     queryset = Mobile.objects.all()

#------------------------------------------------------------------------------------------------------------------
# class MobileViewSet(viewsets.ViewSet):

#     def list(self,request):
#         queryset = Mobile.objects.all()
#         print(queryset)
#         serializer = MobileSerializer(queryset,many=True)
#         return Response(serializer.data)

#     def create(self,request):
#         serializer = MobileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self,request,pk=None):
#         try:
#             mobile = Mobile.objects.get(pk=pk)
#         except Mobile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MobileSerializer(mobile)
#         return Response(serializer.data)
    


#     def update(self,request,pk=None):
#         try:
#             mobile = Mobile.objects.get(pk=pk)
#         except Mobile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MobileSerializer(mobile,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
    
#     def partial_update(self,request,pk=None):
#         try:
#             mobile = Mobile.objects.get(pk=pk)
#         except Mobile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = MobileSerializer(mobile,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     def destroy(self,request,pk=None):
#         try:
#             mobile = Mobile.objects.get(pk=pk)
#         except Mobile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         mobile.delete()
#         return Response(status=status.HTTP_200_OK)
# # --------------------------------------------------------