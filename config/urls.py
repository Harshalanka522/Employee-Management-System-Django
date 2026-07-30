from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('apps.employees.urls')),
    path('', include('apps.department.urls')),
    path('', include('apps.attendance.urls')),
    path('', include('apps.salary.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
        
]
