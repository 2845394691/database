from django.shortcuts import render, redirect
from django import forms
from myapp import models


class LoginForm(forms.Form):
    staffno = forms.CharField(
        widget=forms.TextInput(attrs={"type": "text", "placeholder": "username"})
    )
    password = forms.CharField(
        # 设置样式属性， render_value使得写了的密码不会消失
        widget=forms.PasswordInput(attrs={"type": "password", "placeholder": "password"}, render_value=True)
    )


def login(request):
    """用户登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 这里获得的是前端返回的数据，已经解码过了，是字典类型，**字典是过滤操作的简便用法
        staff = models.Staff.objects.filter(**form.cleaned_data).first()
        # 用户密码错误时
        if not staff:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户密码正确时
        request.session["info"] = {'id': staff.staffno}
        return redirect("/staff/index/")
    return render(request, 'login.html', {'form': form})
