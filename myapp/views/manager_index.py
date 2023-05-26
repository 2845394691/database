from django.shortcuts import render


# Create your views here.
# 部门负责人首页

def index(request):
    return render(request, 'staff_index.html')
