from django.shortcuts import render, redirect
from myapp.models import Department
from myapp.models import Departmentposition
from myapp import models
import time
import random

def get_rander_num():
    while True:
        # 获取系统当前时间作为种子
        seed = int(time.time())
        # 创建Random对象
        r = random.Random(seed)
        # 生成1000到9999之间的随机数
        result = r.randint(1, 9999)
        object = models.Department.objects.filter(departmentno=result)
        if not object:
            return result

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
    name = request.POST.get('name')
    models.Department.objects.create(departmentno=get_rander_num(), departmentname=name)
    return redirect("/admin/depart/")