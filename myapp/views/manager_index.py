from django.shortcuts import render


# Create your views here.
# 部门负责人首页

def index(request):
    return render(request, 'manager_index.html')


