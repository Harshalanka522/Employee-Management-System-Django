from django import forms
from apps.employees.models import Department



class departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields ='__all__'
