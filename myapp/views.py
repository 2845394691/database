from django.shortcuts import render

# Create your views here.
# bootstrap引入实例
def bootstrap_test(request):
    return render(request,'test.html')

def login(request):
    return render(request,'login.html')

