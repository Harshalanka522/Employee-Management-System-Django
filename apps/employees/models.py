from django.db import models
from apps.department.models import Department
  


class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
         Department,
         on_delete=models.CASCADE
     )
    
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    joining_date = models.DateField()

    def __str__(self):
        return self.name
