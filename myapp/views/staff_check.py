from django.shortcuts import render, redirect
from myapp import models
import time
import random


def get_date():
    t = time.localtime()
    date = "{}-{}-{}".format(t.tm_year, t.tm_mon, t.tm_mday)
    return date


def get_time():
    t = time.localtime()
    now_time = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
    return now_time


def get_rander_num():
    while True:
        # 获取系统当前时间作为种子
        seed = int(time.time())
        # 创建Random对象
        r = random.Random(seed)
        # 生成1000到9999之间的随机数
        result = r.randint(1, 9999)
        object = models.Attendancerecord.objects.filter(recordno=result)
        if not object:
            return result


def staff_check(request):
    """员工当日考勤"""
    cookie_dict = request.session['info']
    staffno = cookie_dict['id']
    staff = models.Staff.objects.get(staffno=staffno)

    date = get_date()
    flag = models.Attendancerecord.objects.filter(staffno=staffno, recorddate=date).filter()
    if not flag:
        models.Attendancerecord.objects.create(recordno=get_rander_num(), staffno=staff, recorddate=date)

    checks = models.Attendancerecord.objects.filter(staffno=staffno).order_by("-recorddate").all()
    # 前端要展示的列表数据
    checks_display = []
    for check in checks:
        check_clone = {}
        check_clone['recordNo'] = check.recordno
        check_clone['name'] = check.staffno.staffname
        check_clone['date'] = check.recorddate
        if not check.starttime:
            check_clone['start'] = '未签到'
        else:
            check_clone['start'] = check.starttime
        if not check.endtime:
            check_clone['end'] = '未签退'
        else:
            check_clone['end'] = check.endtime
        checks_display.append(check_clone)

    for i in checks_display:
        print(i['recordNo'])
        print(i['name'])
        print(i['date'])
        print(i['start'])
        print(i['end'])
    return render(request, 'staff_check.html', {'checks': checks_display})


def staff_check_start(request):
    """员工签到"""
    cookie_dict = request.session['info']
    staffno = cookie_dict['id']
    staff = models.Staff.objects.get(staffno=staffno)
    date = get_date()
    flag = models.Attendancerecord.objects.get(staffno=staffno, recorddate=date)
    flag.starttime = get_time()
    flag.save()
    return redirect("/staff/check/")


def staff_check_end(request):
    """员工签退"""
    cookie_dict = request.session['info']
    staffno = cookie_dict['id']
    staff = models.Staff.objects.get(staffno=staffno)
    date = get_date()
    flag = models.Attendancerecord.objects.get(staffno=staffno, recorddate=date)
    flag.endtime = get_time()
    flag.save()
    return redirect("/staff/check/")
