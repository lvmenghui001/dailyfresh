from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from df_car.models import *
from df_user import user_decorator

# 购物车
@user_decorator.login
def car(request):
    user_id = request.session["user_id"]
    cars = CarInfo.objects.filter(user_id=user_id)
    content = {"cars":cars}
    return render(request, "df_car/car.html",content)

# 加入购物车
@user_decorator.login
def add(request,gid,gnum):
    #用户uid买了什么
    user_id = request.session["user_id"]
    gid = int(gid)
    gnum = int(gnum)
    cars = CarInfo.objects.filter(user_id=user_id,goods_id=gid)
    if len(cars)>=1:
        car = cars[0]
        car.count =car.count+gnum
    else:
        car = CarInfo()
        car.user_id = user_id
        car.count = gnum
        car.goods_id = gid
    car.save()
    # 如果是ajax请求返回json数据
    count = CarInfo.objects.filter(user_id=request.session["user_id"]).count()
    if request.is_ajax():
        return JsonResponse({"count":count})
    else:
        # return render(request,"df_goods/list.html",{"count":count})
        return redirect('/cars/car/')
    # return render(request,"df_goods/detail.html",{"count":count})

# 修改购物车
@user_decorator.login
def edit(request,car_id,count):
    print(count)
    try:
        car = CarInfo.objects.get(id=int(car_id))
        count1=car.count
        car.count=int(count)
        car.save()
        data = {"ok":1}
    except Exception as e:
        data = {"ok":0}
    return JsonResponse(data)

# 删除购物车
@user_decorator.login
def car_del(request,car_id):
    try:
        car = CarInfo.objects.get(id=car_id)
        car.delete()
        data = {"ok":1}
    except Exception as e:
        data = {"ok":0}
    return JsonResponse(data)