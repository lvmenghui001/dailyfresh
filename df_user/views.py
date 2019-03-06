from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from . models import *
from hashlib import sha1
from . import user_decorator
from df_goods.models import *
from df_orders.models import *

# 显示注册页面
def register(request):
    uname = request.COOKIES.get('uname','')
    context = {"title":'天天生鲜-注册','error_name':0,'error_pwd':0,'uname':uname}
    return render(request, "df_user/register.html", context)

def register_exist(request):
    uname = request.GET.get("name")
    count = UserInfo.objects.filter(uname=uname).count()
    return HttpResponse(json.dumps(count))

# 注册
def register_handle(request):
    #接收用户输入
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uphone = post.get("phone")

    # 判断两次密码
    if upwd != upwd2:
        return redirect("/user/register/")

    # 密码加密
    s1 = sha1()
    s1.update(repr(upwd).encode('utf-8'))
    upwd3 = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uphone = uphone
    try:
        user.save()
    except:
        return redirect("/user/register/")

#注册成功，转到登录页
    return redirect("/user/login/")

# 显示登录页面
def login(request):
    uname = request.COOKIES.get('uname','')
    context = {"title": '天天生鲜-登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, "df_user/login.html", context)

# 登录
def login_handle(request):
    # 接收请求信息
    post = request.POST
    uname = post.get("username")
    upwd = post.get("pwd")
    jizhu = post.get("jizhu",0)

    # 根据用户名查询对象
    user = UserInfo.objects.filter(uname=uname)
    if len(user) == 1:
        # 密码加密后对比
        s1 = sha1()
        s1.update(repr(upwd).encode('utf-8'))
        upwd3 = s1.hexdigest()
        if upwd3 == user[0].upwd:
            red = request.COOKIES.get("url","/")
            red = HttpResponseRedirect(red)
            # 记住用户名
            if jizhu!=0:
                red.set_cookie('name',uname)
            else:
                red.set_cookie('name','',max_age=-1)
            request.session['user_id']=user[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {"title": '天天生鲜-注册', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {"title": '天天生鲜-注册','error_name': 1,'error_pwd': 0,'uname': uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)


#退出登录
def logout(request):
    request.session.flush()
    return redirect("/")


# 用户个人信息
@user_decorator.login
def info(request):
    #最近浏览
    user_id = request.session["user_id"]
    goods_ids = UserInfo.objects.get(id=user_id).uhistory
    goods_ids1 = goods_ids.split(",")
    goods_list = []
    user_id = request.session["user_id"]
    user = SiteInfo.objects.filter(user=user_id,isDefault=1)
    if user:
        user = user[0]
    else:
        user = SiteInfo.objects.filter(user=user_id).order_by("id")
        if user:
            user = user[0]
        else:
            user = ""

    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(str(goods_id))))
    content = {
        "title":"用户中心",
        "user":user,
        "goods_list":goods_list,
    }
    return render(request,"df_user/user_center_info.html",content)


# 全部订单
@user_decorator.login
def order(request):
    

    return render(request,"df_user/user_center_order.html")


# 收货地址
@user_decorator.login
def site(request):
    user_id = request.session["user_id"]
    user = SiteInfo.objects.filter(user=user_id,isDefault=1)
    site_all = SiteInfo.objects.filter(user=user_id)
    if user:
        user = user[0]
    else:
        user = SiteInfo.objects.filter(user=user_id).order_by("id")
        if user:
            user = user[0]
        else:
            user = ""
        site_all = ""
    return render(request,"df_user/user_center_site.html",{"user":user,"site_all":site_all})


def add_info(request):
    print(request.POST)
    if "isDefault" in request.POST:
        SiteInfo.objects.update(isDefault=0)
        isDefault = 1
    else:
        isDefault = 0
    user_id=request.session["user_id"]
    user = SiteInfo(
        uname = request.POST["uname"],
        uaddress = request.POST["uaddress"],
        uyoubian = request.POST["uyoubian"],
        uphone = request.POST["uphone"],
        user_id = user_id,
        isDefault = isDefault
    )
    user.save()
    return redirect("/user/info/")

from .send_message import *
import json
def sendCode(request):
    phone = request.GET["phone"]
    identify_code = main(phone)
    return HttpResponse(json.dumps(identify_code))

# 省市区选择
def province(request):
    prolist = AreaInfo.objects.filter(parea__isnull=True)
    # data = {"data":data}
    list = []
    # [[1,"北京"],[2,"天津"]]
    for item in prolist:
        list.append([item.id,item.title])
    return JsonResponse({"data":list})

def city(request,id):
    citylist = AreaInfo.objects.filter(parea_id = id)
    list=[]
    # [{id:1,title:"北京"},{},{}]
    for item in citylist:
        list.append({"id":item.id,"title":item.title})
        # {data: [{id: 1, title: "北京"}, {id: 1, title: "天津"}, ...]}
    return JsonResponse({"data":list})


def site_del(request,site_id):
    try:
        site = SiteInfo.objects.get(id=site_id)
        site.delete()
        data = {"ok":1}
    except Exception as e:
        data = {"ok":0}
    return JsonResponse(data)