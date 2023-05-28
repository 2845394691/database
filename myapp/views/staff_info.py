from django.shortcuts import render
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
