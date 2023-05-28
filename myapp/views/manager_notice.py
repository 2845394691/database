import time
import random
import datetime
from django.shortcuts import render,redirect
from myapp.models import Manager, Department
from myapp.models import Mail
from myapp.models import Staff


def publish(request):
    if request.method == "GET":
        # 获取负责人id
        var = request.session.get('info')
        manager_id = var['id']
        # 获取负责人名字列表
        managerset = list(Manager.objects.filter(staffno=manager_id).values_list('staffname', flat=True))
        # 获取部门编号列表
        departnotset = list(Manager.objects.filter(staffno=manager_id).values_list('departmentno', flat=True))
        departno = departnotset[0]
        # 获取部门名字列表
        departnameset = list(Department.objects.filter(departmentno=departno).values_list('departmentname', flat=True))

        return render(request, 'manager_notice_publish.html', {"mname":managerset,"dname":departnameset})

    # 获取负责人id
    var = request.session.get('info')
    manager_id = var['id']
    manager = Staff.objects.filter(staffno=manager_id).first()
    # 获取负责人名字列表
    managerset = list(Manager.objects.filter(staffno=manager_id).values_list('staffname', flat=True))
    # 获取部门编号列表
    departnotset = list(Manager.objects.filter(staffno=manager_id).values_list('departmentno', flat=True))
    departno = departnotset[0]
    # 获取部门名字列表
    departnameset = list(Department.objects.filter(departmentno=departno).values_list('departmentname', flat=True))
    # 获取表单值
    content = request.POST.get('content')
    # 获取当前日期
    current_date = datetime.date.today()
    # 获取当前时间
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    # 获取系统当前时间作为种子
    seed = int(time.time())
    # 创建Random对象
    r = random.Random(seed)
    # 生成1000到9999之间的随机数
    result = r.randint(1, 9999)

    # 插入数据库  staffno=staff_id,man_staffno=manager,
    mail = Mail(mailno=result, staffno=manager, arrivaldate=current_date,arrivaltime=current_time,
                mailcontent=content,mailtype=departnameset[0])
    mail.save()

    return render(request, 'manager_notice_publish.html', {"mname": managerset, "dname": departnameset})


def detail(request):
    manage = request.session["info"]
    manage_id = manage['id']
    mail=Mail.objects.filter(staffno=manage_id)

    return render(request, 'manage_notice_detail.html', {'mail': mail})

def chehui(request):
    mailno = request.GET.get('nid')
    Mail.objects.filter(mailno=mailno).delete()
    return redirect("/manager/notice/detail/")

