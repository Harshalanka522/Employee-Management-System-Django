from django.urls import path
from apps.api import views 


urlpatterns = [

    
  # EMPLOYEES :
  path('getemployee/', views.getemployee),
  path('oneemployee/<int:pk>/', views.oneemployee),

  #DEPARTMENT:
  path('getdepartments/', views.getdepartment),
  path('onedep/<int:pk>/', views.onedep),


  # ATTENDANCE  CLASS BASED APIVIEWS :
  path('getattendance/', views.attends.as_view()),



      
]