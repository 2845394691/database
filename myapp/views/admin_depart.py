from django.shortcuts import render,redirect
from myapp.models import Department
from myapp.models import Departmentposition

def detail(request):
    if request.method=="GET":
        return render(request,"admin_depart.html")


