from django.shortcuts import render


# Create your views here.
# 管理员首页

def index(request):
    return render(request, 'staff_index.html')

