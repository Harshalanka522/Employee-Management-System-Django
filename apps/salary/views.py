from django.shortcuts import render,redirect
from apps.salary.forms import Salaryform
from apps.salary.models import Salary
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.


@permission_required('salary.add_salary')
def salary_form(request):
    form = Salaryform
    if request.method == 'POST':
        form = Salaryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salarylist')
    F = {'S':form}
    return render(request,'salary/salaryform.html',F)



@permission_required('salary.view_salary')
def salarylist(request):
    query = request.GET.get('search', '')
    salaries = Salary.objects.all()
    if query:
        salaries = salaries.filter(
            Q(employee__name__icontains=query) |
            Q(salary_month__icontains=query) |
            Q(salary_year__icontains=query)
        )
    return render(request, 'salary/salarylist.html', {'salaries': salaries})



@permission_required('salary.change_salary')
def updatesalary(request,gid):
    data = Salary.objects.get(id=gid)
    form = Salaryform(instance=data)
    if request.method == 'POST':
        form=Salaryform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Salary updated succesfully")
            return redirect('salarylist')
    a ={'S':form}
    return render(request,'salary/salaryform.html',a)


@permission_required('salary.delete_salary')
def deletesalary(request,gid):
     d = Salary.objects.get(id=gid)
     d.delete()
     messages.success(request,"Salary Deleted Successfully")
     return redirect('salarylist')
