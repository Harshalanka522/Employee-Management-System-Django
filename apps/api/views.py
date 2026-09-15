from django.shortcuts import render
from apps.employees.models import Employee
from apps.api.serializers import Employeeserializer,Departmentserializer,Attendanceserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apps.department.models import Department
from apps.attendance.models import Attendance


# Create your views here.


@api_view(['GET','POST'])
def getemployee(request):
    if request.method == 'GET':
     employe = Employee.objects.all()
     serializer = Employeeserializer(employe,many=True)
     return Response(serializer.data,status=status.HTTP_200_OK)  

    elif request.method == 'POST':
       serializer =Employeeserializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)

       return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT','DELETE'])
def oneemployee(request,pk):
    try:
       std = Employee.objects.get(pk=pk) 
    except Employee.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method =='GET':
       serializer =Employeeserializer(std)
       return Response(serializer.data,status=status.HTTP_200_OK)  

    elif request.method == 'PUT':
          serializer =Employeeserializer(std,data=request.data)
          if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method =='PATCH':
       serializer=Employeeserializer(data=request.data,partial=True)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_200_OK)
            


    elif request.method == 'DELETE':
       std.delete()
       return Response(status=status.HTTP_400_BAD_REQUEST)


    

@api_view(['GET','POST'])
def getdepartment(request):
   if request.method == 'GET':
      dep = Department.objects.all()
      serializer = Departmentserializer(dep,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   elif request.method == 'POST':
      serializer=Departmentserializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors,statuse=status.HTTP_400_BAD_REQUEST)
      

@api_view(['GET','PUT','DELETE'])
def onedep(request,pk): 
   try:
      dep =Department.objects.get(pk=pk)  

   except Department.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
      serializer=Departmentserializer(dep)
      return Response(serializer.data,status=status.HTTP_200_OK)

   elif request.method == 'PUT':
      serializer=Departmentserializer(dep,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      else:
         return Response(status=status.HTTP_204_NO_CONTENT)
      

   elif request.method == 'DELETE':
      dep.delete()
      return Response(status=status.HTTP_400_BAD_REQUEST)   
   

class attends(APIView):
   def get(self,request):
      attend = Attendance.objects.all()
      serializer = Attendanceserializer(attend,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

   def post(self,request):
      serializer=Attendanceserializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
         
       