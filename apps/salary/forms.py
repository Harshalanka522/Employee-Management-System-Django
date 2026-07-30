from django import forms
from apps.salary.models import Salary


class Salaryform(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'
        