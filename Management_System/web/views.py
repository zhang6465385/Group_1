from django.shortcuts import render,redirect
from django.views import View
# from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from web.models import *
import re

class Parents_Register(View):
    def get(self,request):
        return render(request,"user/register.html")
    def post(self,request):
        mes = ""
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_Password = request.POST.get("confirm_Password")
        if all([username,password,confirm_Password]):
            uname = Parents.objects.filter(username=username)
            if not uname:
                if password == confirm_Password:
                    if len(password) >= 6:
                        parent = Parents(username=username, password=password, confirm_Password=password)
                        parent.save()
                        return redirect("/teacher_login/")
                    else:
                        mes = "密码长度有问题"
                else:
                    mes = "俩次密码不一致"
            else:
                mes = "用户名已经存在"
        else:
            mes = "信息不全"
        return render(request,"user/register.html",{"mes":mes})

# 家长登陆
class Parents_Login(View):
    def get(self,request):
        return render(request,"user/login.html")
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if all([username, password]):
            u = Parents.objects.filter(user_name=username).first()
            if u:
                if password == u.password:
                    request.session["username"] = username
                    request.session["user_id"] = u.id
                    mes = "登录成功"
                    mes = "登录成功"
                    return redirect('/')
                else:
                    mes = "密码不正确"
            else:
                mes = "账号不存在"
        else:
            mes = "信息不全"
        return render(request,"user/login.html",locals())
