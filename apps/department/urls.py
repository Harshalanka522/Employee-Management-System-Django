from django.urls import path
from apps.department import views

urlpatterns = [
         path('department/', views.department, name='department'),
         path('departhome/', views.depart, name='departhome'),
         path('departmentlist/', views.departmentlist, name='departlist'),
         path('department/update/<int:did>/', views.updatedep, name='updatelist'),
         path('department/delete/<int:did>/', views.deletedep, name='deletedip'),
                    
                  
           
]