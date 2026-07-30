from django.db import models
from apps.employees.models import Employee

# Create your models here.

ds = [
    ('PRESENT','Present'),
    ('ABSENT','Absent'),
    ('HALF-DAY','Half-day'),
    ('LEAVE','Leave'),
]


class Attendance(models.Model):
    employeename=models.ForeignKey(
      Employee,on_delete=models.CASCADE
   )
    date = models.DateField()
    status = models.CharField(max_length = 40 ,choices=ds)

def __str__(self):
    return f"{self.employeename.name} - {self.date}"    
