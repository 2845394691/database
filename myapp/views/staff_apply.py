from django.shortcuts import render,redirect
from myapp.models import Absence
from myapp.models import Staff
from myapp.models import Department
from myapp.models import Manager
import datetime
import time,random


# Create your views here.

# 员工请假表
def qingjia(request):
    if request.method == 'GET':
        # 获取员工id
        var = request.session.get('info')
        staff_id = var['id']
        # staff=Staff.objects.filter(staffno=staff_id).first()
        # 获取员工名字列表
        staffset=list(Staff.objects.filter(staffno=staff_id).values_list('staffname',flat = True))
        # 获取部门编号列表
        departnotset=list(Staff.objects.filter(staffno=staff_id).values_list('departmentno',flat = True))
        departno=departnotset[0]
        # 获取部门名字列表
        departnameset=list(Department.objects.filter(departmentno=departno).values_list('departmentname',flat = True))


        return render(request, 'staff_qingjia.html', {"sname":staffset,"dname":departnameset})

    # 处理表单数据

    # 获取员工id
    staff_info = request.session.get('info')
    staff_id = staff_info['id']
    staff=Staff.objects.filter(staffno=staff_id).first()
    # 获取员工名字列表
    staffset = list(Staff.objects.filter(staffno=staff_id).values_list('staffname', flat=True))
    # 获取部门编号列表
    departnotset = list(Staff.objects.filter(staffno=staff_id).values_list('departmentno', flat=True))
    departno = departnotset[0]
    # 获取部门名字列表
    departnameset = list(Department.objects.filter(departmentno=departno).values_list('departmentname', flat=True))
    # 获取员工主管id
    managerset = list(Staff.objects.filter(staffno=staff_id).values_list('man_staffno', flat=True))
    managerno = managerset[0]
    manager=Manager.objects.filter(staffno= managerno).first()
    # 获取表单值
    start_date=request.POST.get('start_data')
    end_data=request.POST.get('end_data')
    reason=request.POST.get('reason')
    # 获取当前日期
    current_date = datetime.date.today()
    #
    # 获取系统当前时间作为种子
    seed = int(time.time())
    # 创建Random对象
    r = random.Random(seed)
    # 生成1000到9999之间的随机数
    result = r.randint(1, 9999)

    # 插入数据库  staffno=staff_id,man_staffno=manager,
    absense=Absence(abno=result,staffno=staff,man_staffno=manager,abreason=reason,abapplydate=current_date,abstartdate=start_date,abenddate=end_data,abstatu="未审核")
    absense.save()
    return render(request,'staff_qingjia.html', {"sname":staffset,"dname":departnameset})
    # redirect("staff/apply/qingjia/")
