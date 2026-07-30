from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.attendance.forms import Attendanceform
from apps.attendance.models import Attendance
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.

@permission_required('attendance.add_attendance')
def attendance(request):
    form = Attendanceform
    if request.method == 'POST':
           form = Attendanceform(request.POST)
           if form.is_valid():
                form.save()
                return redirect('attendancelist')
    D = {'you':form}
    return render(request,'attendance/attendance.html',D)

@permission_required('attendance.view_attendance')
def attendancelist(request):
     search = request.GET.get('search')
     d = Attendance.objects.all()
     if search:
          d = Attendance.objects.filter(
            Q(employeename__name__icontains=search) |
            Q(status__icontains=search) |
            Q(date__icontains=search)
          )

     s = {'attendancelist':d}
     return render(request,'attendance/attendancelist.html',s)


@permission_required('attendance.change_attendance')
def updateattendance(request,sid):
     s = Attendance.objects.get(id=sid)
     form = Attendanceform(instance=s)
     if request.method=='POST':
          form=Attendanceform(request.POST,instance=s)
          if form.is_valid():
               form.save()
               messages.success(request,"Attendance updated successfully")
               return redirect('attendancelist')
     F = {'you':form}  
     return render(request,'attendance/attendance.html',F)    


@permission_required('attendance.delete_attendance')
def deleteattendance(request,eid):
     g = Attendance.objects.get(id=eid)
     g.delete()
     messages.success(request,"Attendance Deleted successfully")
     return redirect('attendancelist')

     
     