from django.shortcuts import render,redirect
from myapp.models import Meeting
from myapp.models import Staff
from myapp.models import Department
from myapp.models import Manager
import datetime
import random
import time

def publish(request):
    # 获取负责人id
    var = request.session.get('info')
    staff_id = var['id']
    staff=Manager.objects.filter(staffno=staff_id).first()
    # 获取员工名字列表
    staffset = list(Staff.objects.filter(staffno=staff_id).values_list('staffname', flat=True))
    # 获取部门编号列表
    departnotset = list(Staff.objects.filter(staffno=staff_id).values_list('departmentno', flat=True))
    departno = departnotset[0]
    # 获取部门名字列表
    departnameset = list(Department.objects.filter(departmentno=departno).values_list('departmentname', flat=True))

    if request.method == 'GET':

        return render(request, 'manager_meeting_publish.html', {"sname": staffset, "dname": departnameset})


    # 获取表单值
    title=request.POST.get('title')
    start_date=request.POST.get('start_date')
    start_time=request.POST.get('start_time')
    end_time=request.POST.get('end_time')
    content = request.POST.get('content')

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
    meeting = Meeting(meetingno=result,staffno=staff,meetingname=title,meetingstarttime=start_time,
                      meetingendtime=end_time,meetingdate=start_date,meetingcontent=content,)
    meeting.save()
    return redirect("/manager/meeting/detail/")

def detail(request):
    # 获取负责人id
    var = request.session.get('info')
    staff_id = var['id']
    meetingset=Meeting.objects.filter(staffno=staff_id)
    return render(request,'manager_meeting_detail.html',{"meetingset":meetingset})

def delete(request):
    meetno = request.GET.get('nid')
    Meeting.objects.filter(meetingno=meetno).delete()
    return redirect("/manager/meeting/detail/")