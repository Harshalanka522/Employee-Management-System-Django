from django.urls import path
from apps.employees import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Employeelist/', views.employee_list, name='employeelist'),
    path('AddEmployee/', views.add_employee, name='AddEmployee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
        
]

