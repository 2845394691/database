from django.shortcuts import render, redirect
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
        object = models.Staff.objects.filter(staffno=result)
        if not object:
            return result


def staff_list(request):
    """展示员工信息"""
    manage = request.session["info"]
    manage_id = manage['id']
    staffs = models.Staff.objects.filter(man_staffno=manage_id)

    return render(request, 'manage_staff_list.html', {'staffs': staffs})


def staff_add(request):
    """添加员工"""
    manage_dict = request.session['info']
    manage = models.Manager.objects.get(staffno=manage_dict['id'])
    depart_name = manage.departmentno.departmentname
    if request.method == 'GET':
        return render(request, 'manage_staff_add.html',
                      {'depart_name': depart_name, })
    name = request.POST.get('name')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    position = request.POST.get('position')
    position_object = models.Departmentposition.objects.get(departmentno=manage.departmentno, positionname=position)
    gender = request.POST.get('gender')
    staffno = get_rander_num()
    models.Staff.objects.create(staffno=staffno,
                                departmentno=manage.departmentno,
                                positionno=position_object,
                                man_staffno=manage,
                                staffname=name,
                                password=password,
                                phoneno=phone,
                                email=email,
                                sex=gender)
    return redirect("/manager/staff/list/")

def staff_delete(request):
    staffno = request.GET.get('nid')
    models.Staff.objects.filter(staffno=staffno).delete()
    return redirect("/manager/staff/list/")

