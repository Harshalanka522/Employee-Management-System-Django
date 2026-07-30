from django.urls import path
from apps.attendance import views

urlpatterns = [
                 
           path('attendanceform/', views.attendance, name='attendanceform'),
           path('attendacelist/', views.attendancelist, name='attendancelist'),
           path('updateattendance/<int:sid>/', views.updateattendance, name='updateattendance'),
           path('deleteattendance/<int:eid>/', views.deleteattendance, name='deleteattendance'),
                               
                                      
           
]