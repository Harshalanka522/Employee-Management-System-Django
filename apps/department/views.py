from django.shortcuts import render,redirect
from apps.department.forms import departmentform
from django.http import HttpResponse
from apps.department.models import Department
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def depart(request):
    return render(request,'departments/departmentshome.html')





@permission_required('department.add_department', raise_exception=True)
def department(request):
    form = departmentform
    if request.method == 'POST':
        form = departmentform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Department added succesfully ")
            return redirect('departhome')    

    D = { 'my':form}
    return render(request,'departments/departments.html',D)




@permission_required('department.view_department', raise_exception=True)
def departmentlist(request):
    search = request.GET.get('Search')
    s = Department.objects.all()
    if search:
        s = Department.objects.filter(
            Q(id__icontains=search) |
            Q(department_name__icontains=search)
            )
   
    return render(request,'departments/departmentlist.html',{'my':s})


@permission_required('department.change_department', raise_exception=True)
def updatedep(request,did):
      s = Department.objects.get(id=did)
      form = departmentform(instance=s)
      if request.method == 'POST':
          form=departmentform(request.POST,instance=s)
          if form.is_valid():
              form.save()
              messages.success(request,"Department updated succesfully")
              return redirect('departlist')
            
      forms = {'my':form}
      return render(request,'departments/departments.html',forms)



@permission_required('department.delete_department', raise_exception=True)
def deletedep(request,did):
    d = Department.objects.get(id=did)
    d.delete()
    messages.success(request,"Department deleted succesfully")
    return redirect('departlist')
