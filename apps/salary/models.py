from django.db import models
from apps.employees.models import Employee


# Create your models here.



class Salary(models.Model):
    MONTHS = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    salary_month = models.CharField(max_length=20,choices=MONTHS)
    salary_year = models.CharField(max_length=4, default='2026')
    basic_salary = models.DecimalField( max_digits=10, decimal_places=2)
    bonus = models.DecimalField( max_digits=10, decimal_places=2,default=0)
    deduction = models.DecimalField( max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField( max_digits=10,decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.net_salary = self.basic_salary + self.bonus - self.deduction
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.employee.name} - {self.salary_month}"
