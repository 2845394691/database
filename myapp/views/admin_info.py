from django.shortcuts import render,redirect
from myapp.models import Staff,Manager

def manager(request):
    manager=Manager.objects.all()
    return render(request,'admin_info_manager.html',{"manager":manager})

def manager_del(request):
    managerno=request.GET.get('nid')
    Staff.objects.filter(staffno=managerno).delete()
    return redirect("/admin/info/manager/")

def staff(request):
    staff=Staff.objects.filter(man_staffno__isnull=False)
    return render(request,'admin_info_staff.html',{"staff":staff})

def staff_del(request):
    staffno=request.GET.get('nid')
    Staff.objects.filter(staffno=staffno).delete()
    return redirect("/admin/info/staff/")




