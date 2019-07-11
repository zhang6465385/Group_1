from django.shortcuts import render,redirect
# from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from web.models import *
import re
def index(request):
    user_id = request.session.get('t_id')
    if not user_id:
        return redirect('/sadmin/teacher_login/')
    return render(request,'sadmin/index.html')

# 老师登陆

def Teacher_Login(request):
    if request.method == "GET":
        return render(request,"sadmin/page_login.html")
    if request.method == "POST":
        error_data = {}
        work_number = request.POST.get("work_number")
        password = request.POST.get("password")
        if not all([ password,work_number]):
            if not password:
                error_data["password"] = {"error":"密码为空"}
            if not work_number:
                error_data["work_number"] = {"error":"学号为空"}
            return render(request,"sadmin/page_login.html",locals())
        else:
            u = Teacher.objects.filter(work_number=work_number).first()
            if u:
                if password == u.password:
                    request.session["t_id"] = u.id
                    return redirect("/index/")
                else:
                    error_data["password"] = {"error":"密码错误"}
            else:
                error_data["work_number"] = {"error": "此学号未存在"}
        return render(request,"sadmin/page_login.html",locals())