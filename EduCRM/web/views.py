from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
from web.models import *
import re
from django.http import HttpResponse

def Object(request):
    return render(request,"user/pay.html")

def no_login(views):
    def warpper(request,*args,**kwargs):
        if request.session.get("user_id"):
            return redirect("/object/")
        else:
            return views(request,*args,**kwargs)
    return warpper

def had_login(views):
    def warpper(request,*args,**kwargs):
        #判断当前用户是否登陆
        if request.session.get('user_id'):
            return views(request,*args,**kwargs)
        else:
            return redirect('/parents_login/')
    return warpper


@no_login
def Parents_Register(request):
    if request.method == "GET":
        return render(request,"user/register.html")
    if request.method == "POST":
        error_data = {}
        parents_name = request.POST.get("parents_name")
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        id_card = request.POST.get("id_card")
        confirm_password = request.POST.get("confirm_password")
        if not all([parents_name,user_name,password,id_card]):
            if not parents_name:
                error_data['parents_name'] = {'error':'账号未填写'}
            if not user_name:
                error_data["user_name"] = {'error': '用户名未填写'}
            if not password:
                error_data['password'] = {'error': '密码未填写'}
            if not confirm_password:
                error_data["confirm_password"] = {"error":"确认密码未填写"}
            if not id_card:
                error_data["id_card"] = {'error': '身份证未填写'}
            return render(request, "user/register.html", locals())
        try:
            if re.match("[\u4e00-\u9fa5]+",parents_name):
                if len(parents_name) <= 5:
                    u = Parents.objects.filter(user_name=user_name).first()
                    if not u:
                        if re.match("^[a-zA-Z][a-zA-Z0-9_]*$",user_name):
                            if len(user_name)>=6 and len(user_name)<=12:
                                if re.match('^(\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$',id_card):
                                    if len(id_card) == 18:
                                        card = Parents.objects.filter(id_card=id_card).first()
                                        if not card:
                                            if re.match('^(?=.*\d)(?=.*[A-Z]).{8,10}$', password):
                                                if len(password) >= 8 and len(password)<=12:

                                                    if password == confirm_password:
                                                        passwords = make_password(password)
                                                        parents = Parents(parents_name=parents_name,user_name=user_name,id_card=id_card,password=passwords)
                                                        parents.save()
                                                        return redirect("/parents_login/")
                                                    else:
                                                        error_data["confirm_password"] = {"error":"密码不一样"}

                                                else:
                                                    error_data["password"] = {"error":"密码长度有误"}
                                            else:
                                                error_data["password"] = {"error":"密码格式有误"}
                                        else:
                                            error_data["id_card"] = {"error":"此身份证已经被注册"}
                                    else:
                                        error_data["id_card"] = {"error":"身份证长度有误"}
                                else:
                                    error_data["id_card"] = {"error":"身份证格式有误"}
                            else:
                                error_data["user_name"] = {"error":"用户名长度有误"}
                        else:
                            error_data["user_name"] = {"error":"用户名证格式有误"}
                    else:
                        error_data["user_name"] = {"error": "此用账号已经被注册"}
                else:
                    error_data["parents_name"] = {"error":"姓名长度超出范围"}
            else:
                error_data["parents_name"] = {"error":"账号，请重新输入"}
        except:
            pass
        return render(request,"user/register.html",locals())


# 家长登陆
@no_login
def Parents_Login(request):
    if request.method == "GET":
        return render(request,"user/login.html")
    if request.method == "POST":
        mes = ""
        error_data = {}
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        if not all([user_name, password]):
            if not user_name:
                error_data["user_name"] = {"error":"账号为空"}
            if not password:
                error_data["password"] = {"error":"密码为空"}
            return render(request,"user/login.html",locals())
        else:
            try:
                u = Parents.objects.filter(user_name=user_name)
                if u:
                    pass
                    if check_password(password,u.password):
                        u.password = make_password(password)
                        u.save()
                        request.session["user_name"] = user_name
                        request.session["user_id"] = u.id
                        print(u.id)
                        return redirect("/object/")
                    else:
                        error_data["password"] = {"error":"密码错误"}
                else:
                    error_data["user_name"] = {"error": "此账号未存在"}
            except:
                mes = "输入有误"
        return render(request,"user/login.html",locals())

@had_login
def logout(request):
    del request.session["user_id"]
    return redirect('/parents_login/')



