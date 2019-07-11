from django.shortcuts import render,redirect
from django.views import View
# from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from web.models import *
import re
def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/sadmin/teacher_login/')
    return render(request,'sadmin/index.html')

# 老师登陆
class Teacher_Login(View):
    def get(self,request):
        return render(request,"sadmin/page_login.html")
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if all([username, password]):
            u = Teacher.objects.filter(work_number=username).first()
            if u:
                if password == u.password:
                    request.session["username"] = username
                    request.session["user_id"] = u.id
                    # mes = "登录成功"
                    # mes = "登录成功"
                    return redirect('/')
                else:
                    mes = "密码不正确"
            else:
                mes = "账号不存在"
        else:
            mes = "信息不全"
        return render(request, "sadmin/page_login.html", locals())
