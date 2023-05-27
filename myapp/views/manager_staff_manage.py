from django.shortcuts import render
from myapp import models


def staff_list(request):
    """展示员工信息"""
    manage = request.session["info"]
    manage_id = manage['id']
    staffs = models.Staff.objects.filter(man_staffno=manage_id)

    return render(request, 'manage_staff_list.html', {'staffs': staffs})

def staff_add(request):
    """添加员工"""
    if request.method == 'GET':
        manage_dict = request.session['info']
        manage = models.Manager.objects.get(staffno=manage_dict['id'])
        depart_name = manage.departmentno.departmentname
        depart_position = manage.departmentno.departmentno

        return render(request, 'manage_staff_add.html',
                      {'depart_name':depart_name,
                       'depart_positions':depart_position})

