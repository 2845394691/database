from django.shortcuts import render, redirect
from myapp import models


def salary_list(request):
    cookie_dict = request.session.get('info')
    staffno = cookie_dict['id']
    salary = models.Salary.objects.get(staffno=staffno)
    salary_total = salary.basicsalary + salary.insurance + salary.bonus + salary.supplement + salary.overtimepay
    salary_dict = {
        'salary': salary,
        'salary_total': salary_total,
        'basicsalary': salary.basicsalary,
        'insurance': salary.insurance,
        'bonus': salary.bonus,
        'supplement': salary.supplement,
        'overtimepay': salary.overtimepay,
    }
    return render(request, 'staff_salary.html', salary_dict)


def info_modify(request):
    """修改员工信息"""
    cookie_dict = request.session.get('info')
    staffno = cookie_dict['id']
    staff = models.Staff.objects.get(staffno=staffno)
    if request.method == "GET":
        return render(request, 'staff_info.html', {'staff': staff})

    name = request.POST.get('name')
    password = request.POST.get('password')
    date = request.POST.get('date')
    phone = request.POST.get('phone')
    email = request.POST.get('email')

    staff.staffname = name
    staff.password = password
    staff.entrydate = date
    staff.phoneno = phone
    staff.email = email
    staff.save()
    # return render(request, 'staff_info.html', {'staff':staff})
    return redirect('/staff/index/')
