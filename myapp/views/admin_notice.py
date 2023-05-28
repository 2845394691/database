from django.shortcuts import render,redirect
from myapp.models import Mail

def detail(request):
    mail=Mail.objects.all()
    return render(request,'admin_notice.html',{"mail":mail})

def delete(request):
    mailno = request.GET.get('nid')
    Mail.objects.filter(mailno=mailno).delete()
    return redirect("/admin/notice/")

