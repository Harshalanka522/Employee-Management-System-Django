from django.urls import path
from apps.salary import views

urlpatterns = [

       path('salaryform/', views.salary_form, name='salaryform'),
       path('salarylist/', views.salarylist, name='salarylist'),
       path('updatesalary/<int:gid>/', views.updatesalary, name='updatesalary'),       
       path('deletesalary/<int:gid>/', views.deletesalary, name='deletesalary'),       
              
]