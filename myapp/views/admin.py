from django.shortcuts import render, redirect
from django import forms
from myapp import models


# class LoginForm(forms.Form):
#     adminNo = forms.CharField(
#         widget=forms.TextInput(attrs={"type": "text", "name": "User Name", "placeholder": "username"})
#     )
#     password = forms.CharField(
#         # 设置样式属性， render_value使得写了的密码不会消失
#         widget=forms.PasswordInput(attrs={"type": "password", "name": "Password", "placeholder": "password"},
#                                    render_value=True)
#     )


def login(request):
    """管理员登录"""
    if request.method == "GET":
        return render(request, 'admin_login.html')
    # form = LoginForm(data=request.POST)
    # if form.is_valid():
    #     # 这里获得的是前端返回的数据，已经解码过了，是字典类型，**字典是过滤操作的简便用法
    #     admin = models.Admin.objects.filter(**form.cleaned_data).first()
    #     # 用户密码错误时
    #     if not admin:
    #         form.add_error("password", "用户名或密码错误")
    #         return render(request, 'login.html', {'form': form})
    #
    #     # 用户密码正确时
    #     request.session["info"] = {'id': admin.adminNo}
    #     return redirect("/admin/index/")
    # return render(request, 'admin_login.html', {'form': form})

    form = request.POST
    print(form['adminNo'])
    admin = models.Admin.objects.filter(adminNo=form['adminNo'], password=form['password'])
    if not admin:
        label = '用户名或者密码错误!'
        return render(request, 'admin_login.html', {'label': label})
    else:
        request.session["admin"] = {'id': form["adminNo"]}
        return render(request, 'admin_index.html')
    # return render(request, 'admin_login.html')

# def index(request):
#     """管理员首页"""
#     return render(request, 'staff_index.html')
