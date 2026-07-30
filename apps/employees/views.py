from django.shortcuts import render, redirect, get_object_or_404
from apps.employees.models import Employee
from apps.department.models import Department
from apps.attendance.models import Attendance
from apps.salary.models import Salary
from apps.employees.forms import EmployeeForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,permission_required
@login_required
def home(request):
      total_employees = Employee.objects.count()
      total_departments = Department.objects.count()
      total_attendance = Attendance.objects.count()
      total_salary = Salary.objects.count()

      D = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'total_attendance': total_attendance,
        'total_salary': total_salary,
    }

      return render(request, 'Home.html',D)

@permission_required('employees.view_employee')
def employee_list(request):
    search = request.GET.get('search')
    employees = Employee.objects.all()
    if search:
        employees = Employee.objects.filter(
               Q(name__icontains=search) |
               Q(employee_id__icontains=search)
        )
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
           
    return render(request, 'employes/employeelist.html', {'employees': page_obj})


@permission_required('employees.add_employee', raise_exception=True)
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee addded succesfully")
            return redirect('employeelist')
        else:
            messages.success(request,"please fill the valid details ")

    else :
        form = EmployeeForm()        
    return render(request, 'employes/add-employee.html', {'form': form})


@permission_required('employees.change_employee', raise_exception=True)
def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        my = EmployeeForm(request.POST,instance = employee)
        if my.is_valid():
            my.save()
        messages.success(request,"Employee updated succesfully")    
        return redirect('employeelist')



    form = EmployeeForm(instance=employee)
    return render(request, 'employes/add-employee.html', {'form': form})



@permission_required('employees.delete_employee', raise_exception=True)
def delete_employee(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('employeelist')

