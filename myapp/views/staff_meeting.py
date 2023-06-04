from django.shortcuts import render
from myapp.models import Meeting
from myapp.models import Staff, Manager
import datetime
import time

def get_time():
    t = time.localtime()
    now_time = "{}:{}:{}".format(t.tm_hour, t.tm_min, t.tm_sec)
    return now_time


def start(request):
    # 获取员工id
    staff_info = request.session.get('info')
    staff_id = staff_info['id']
    # 获取员工主管id
    managerset = list(Staff.objects.filter(staffno=staff_id).values_list('man_staffno', flat=True))
    managerno = managerset[0]

    meet = Meeting.objects.filter(meetingdate__gte=datetime.date.today(), staffno=managerno, meetingstarttime__gte=get_time())
    return render(request, "staff_meeting.html", {"meetingset": meet})


def end(request):
    # 获取员工id
    staff_info = request.session.get('info')
    staff_id = staff_info['id']
    # 获取员工主管id
    managerset = list(Staff.objects.filter(staffno=staff_id).values_list('man_staffno', flat=True))
    managerno = managerset[0]

    meet = Meeting.objects.filter(meetingdate__lt=datetime.date.today(), staffno=managerno)
    return render(request, "staff_meeting.html", {"meetingset": meet})
