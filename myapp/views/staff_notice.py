from django.shortcuts import render
from myapp.models import Mail
from myapp.models import Staff
from myapp.models import Department

def detail(request):
    var = request.session.get('info')
    staff_id = var['id']
    # 获取部门编号列表
    departnotset = list(Staff.objects.filter(staffno=staff_id).values_list('departmentno', flat=True))
    departno = departnotset[0]
    # 获取部门名字列表
    departnameset = list(Department.objects.filter(departmentno=departno).values_list('departmentname', flat=True))

    mailset=Mail.objects.filter(mailtype=departnameset[0]).order_by("-arrivaldate")

    return render(request, 'staff_notice.html', {'mail': mailset})
