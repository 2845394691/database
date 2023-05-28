from django.shortcuts import render, redirect
from myapp.models import Department
from myapp.models import Departmentposition
from myapp import models


def detail(request):
    """部门管理"""
    departs = models.Department.objects.all()
    total_count_depart = departs.count()
    total_count_staff = 0
    depart_names = []
    depart_counts = []
    for depart in departs:
        staff_count = models.Staff.objects.filter(departmentno=depart.departmentno).count()
        depart_names.append(depart.departmentname)
        depart_counts.append(staff_count)
        total_count_staff = total_count_staff + staff_count
    if request.method == "GET":
        return render(request, "admin_depart.html",
                      {'names': depart_names, 'counts': depart_counts, 'depart_count': total_count_depart,
                       'staff_count':total_count_staff})
