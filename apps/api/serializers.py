from rest_framework import serializers
from apps.employees.models import Employee
from apps.department.models import Department
from apps.attendance.models import Attendance

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class Departmentserializer(serializers.ModelSerializer) :
    class Meta:
        model = Department
        fields = '__all__' 


class Attendanceserializer(serializers.ModelSerializer):
    class Meta:           
        model = Attendance
        fields = '__all__'