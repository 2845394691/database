"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from myapp.views import test
from myapp.views import login
from myapp.views import staff_index
from myapp.views import admin
from myapp.views import admin_index
from myapp.views import manager_index
from myapp.views import staff_apply
from myapp.views import manager_staff_manage
from myapp.views import manager_apply
from myapp.views import staff_info

urlpatterns = [
    # path('admin/', admin.site.urls),
    # bootstrap引入示例
    path('bootstrap/test/', test.bootstrap_test),

    # 用户登录界面
    path('login/', login.login),
    path('', login.login),

    # 用户首页
    path('staff/index/', staff_index.index),

    # 用户请假申请
    path('staff/apply/qingjia/', staff_apply.qingjia),

    # 用户加班申请
    path('staff/apply/jiaban/', staff_apply.jiaban),

    # 部门负责人首页
    path('manager/index/', manager_index.index),

    # 管理员登录
    path('admin/login/', admin.login),

    # 管理员首页
    path('admin/index/', admin_index.index),

    # 部门
    path('manager/staff/list/', manager_staff_manage.staff_list),

    # 用户报销申请
    path('staff/apply/baoxiao/', staff_apply.baoxiao),

    # 用户出差申请
    path('staff/apply/chuchai/', staff_apply.chuchai),

    # 用户辞职申请
    path('staff/apply/cizhi/', staff_apply.cizhi),

    # 负责人添加员工
    path('manager/staff/add/', manager_staff_manage.staff_add),

    # 负责人删除员工
    path('manager/staff/delete/', manager_staff_manage.staff_delete),

    # 负责人审批请假单,请假同意，请假拒绝
    path('manager/apply/qingjia/', manager_apply.qingjia),
    path('manager/apply/qingjia/consent/', manager_apply.qingjia_consent),
    path('manager/apply/qingjia/refuse/', manager_apply.qingjia_refuse),

    # 负责人审批加班单,同意，拒绝
    path('manager/apply/jiaban/', manager_apply.jiaban),
    path('manager/apply/jiaban/consent/', manager_apply.jiaban_consent),
    path('manager/apply/jiaban/refuse/', manager_apply.jiaban_refuse),

    # 员工
    path('staff/apply/list/', staff_apply.apply_list),

    # 负责人审批报销单,同意，拒绝
    path('manager/apply/baoxiao/', manager_apply.baoxiao),
    path('manager/apply/baoxiao/consent/', manager_apply.baoxiao_consent),
    path('manager/apply/baoxiao/refuse/', manager_apply.baoxiao_refuse),

    # 负责人审批出差单,同意，拒绝
    path('manager/apply/chuchai/', manager_apply.chuchai),
    path('manager/apply/chuchai/consent/', manager_apply.chuchai_consent),
    path('manager/apply/chuchai/refuse/', manager_apply.chuchai_refuse),

    # 负责人审批辞职单,同意，拒绝
    path('manager/apply/cizhi/', manager_apply.cizhi),
    path('manager/apply/cizhi/consent/', manager_apply.cizhi_consent),
    path('manager/apply/cizhi/refuse/', manager_apply.cizhi_refuse),

    # 员工工资
    path('staff/salary/', staff_info.salary_list),

]
