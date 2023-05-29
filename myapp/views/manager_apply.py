from django.shortcuts import render, redirect

from myapp.models import Absence
from myapp.models import Department
from myapp.models import Manager
from myapp.models import Staff
from myapp.models import Overtime
from myapp.models import Reimbursement
from myapp.models import Businesstrip
from myapp.models import Leave


def qingjia(request):
    # 获取管理员id
    var = request.session.get('manage')
    manager_id = var['id']
    apply_qingjia = Absence.objects.filter(man_staffno=manager_id, abstatu="未审核").order_by("-abapplydate")
    return render(request, 'manager_qingjia.html', {"apply_qingjia": apply_qingjia})


def qingjia_consent(request):
    abno = request.GET.get('nid')
    Absence.objects.filter(abno=abno).update(abstatu="审核通过")
    return redirect("/manager/apply/qingjia/")


def qingjia_refuse(request):
    abno = request.GET.get('nid')
    Absence.objects.filter(abno=abno).update(abstatu="审核失败")
    return redirect("/manager/apply/qingjia/")


def jiaban(request):
    # 获取管理员id
    var = request.session.get('manage')
    manager_id = var['id']
    apply_jiaban = Overtime.objects.filter(man_staffno=manager_id, overstatu="未审核").order_by("-overapplydate")
    return render(request, 'manager_jiaban.html', {"apply_jiaban": apply_jiaban})


def jiaban_consent(request):
    overno = request.GET.get('nid')
    Overtime.objects.filter(overno=overno).update(overstatu="审核通过")
    return redirect("/manager/apply/jiaban/")


def jiaban_refuse(request):
    overno = request.GET.get('nid')
    Overtime.objects.filter(overno=overno).update(overstatu="审核失败")
    return redirect("/manager/apply/jiaban/")


def baoxiao(request):
    # 获取管理员id
    var = request.session.get('manage')
    manager_id = var['id']
    apply_baoxiao = Reimbursement.objects.filter(man_staffno=manager_id, reimstatu="未审核").order_by("-reimapplydate")
    return render(request, 'manager_baoxiao.html', {"apply_baoxiao": apply_baoxiao})


def baoxiao_consent(request):
    baoxiaono = request.GET.get('nid')
    Reimbursement.objects.filter(reimno=baoxiaono).update(reimstatu="审核通过")
    return redirect("/manager/apply/baoxiao/")


def baoxiao_refuse(request):
    baoxiaono = request.GET.get('nid')
    Reimbursement.objects.filter(reimno=baoxiaono).update(reimstatu="审核失败")
    return redirect("/manager/apply/baoxiao/")


def chuchai(request):
    # 获取管理员id
    var = request.session.get('manage')
    manager_id = var['id']
    apply_chuchai = Businesstrip.objects.filter(man_staffno=manager_id, btstatu="未审核").order_by("-btapplydate")
    return render(request, 'manager_chuchai.html', {"apply_chuchai": apply_chuchai})


def chuchai_consent(request):
    chuchaino = request.GET.get('nid')
    Businesstrip.objects.filter(btno=chuchaino).update(btstatu="审核通过")
    return redirect("/manager/apply/chuchai/")


def chuchai_refuse(request):
    chuchaino = request.GET.get('nid')
    Businesstrip.objects.filter(btno=chuchaino).update(btstatu="审核失败")
    return redirect("/manager/apply/chuchai/")


def cizhi(request):
    # 获取管理员id
    var = request.session.get('manage')
    manager_id = var['id']
    apply_cizhi = Leave.objects.filter(man_staffno=manager_id, leavestatu="未审核").order_by("-leaveapplydate")
    return render(request, 'manager_cizhi.html', {"apply_cizhi": apply_cizhi})


def cizhi_consent(request):
    cizhino = request.GET.get('nid')
    Leave.objects.filter(leaveno=cizhino).update(leavestatu="审核通过")
    return redirect("/manager/apply/cizhi/")


def cizhi_refuse(request):
    cizhino = request.GET.get('nid')
    Leave.objects.filter(leaveno=cizhino).update(leavestatu="审核失败")
    return redirect("/manager/apply/cizhi/")
