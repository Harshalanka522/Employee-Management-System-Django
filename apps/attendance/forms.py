from django import forms 
from apps.attendance.models import Attendance


class Attendanceform(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'