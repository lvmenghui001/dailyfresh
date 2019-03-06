import json

from django.shortcuts import render,redirect
from df_orders.models import *
from df_user.models import *
from df_car.models import *
from df_goods.models import *
import time
# Create your views here.

def pay(request):
    # 购买列表商品id列表
    sku_ids = request.POST.getlist('sku_ids')
    sku_ids = [int(item) for item in sku_ids ]

    # 购买商品价格列表
    sku_price = request.POST.getlist('sku_price')
    sku_price = [float(item) for item in sku_price]

    # 购买商品数量
    sku_counts = request.POST.getlist('sku_counts')
    sku_counts = [int(item) for item in sku_counts]

    # 获取用户的收货地址信息
    user_id= request.session["user_id"]
    order = OrderInfo()
    order.oid = str(int(time.time()))
    order.odate=time.strftime('%Y/%m/%d/%H/%M/%S',time.localtime(time.time()))
    order.oIsPay = 0
    order.ototal = sum([a*b for a,b in zip(sku_price,sku_counts)])

    user = SiteInfo.objects.get(user=user_id, isDefault=1)
    print(user)
    if user:
        user = user
    else:
        user = SiteInfo.objects.filter(user=user_id).order_by("id")
        if user:
            user = user[0]
        else:
            user = ""
    order.oaddress = user.id
    order.user_id = user.user_id
    order.save()

    # 商品详情
    num = 0
    for good in sku_ids:
        details = OrderDetailInfo()
        details.goods_id = good
        details.order_id = order.oid
        details.price = sku_price[num]
        details.count = sku_counts[num]
        details.total_price=sku_price[num]*sku_counts[num]
        num+=1
        details.save()

    # 返回订单信息
    orders = OrderDetailInfo.objects.filter(order__oid=str(int(time.time())))
    print(orders[0].price)
    context = {
        "address": user.uaddress,
        "orders": orders,
        "user": user
    }
    return render(request,"df_order/order.html",context)


def buy(request):
    # orders = request.GET.getlist("orders")
    # for order in orders:
    #     dingdan = OrderInfo.objects.get(user__orderinfo__oid=int(order.oid))
    #     dingdan.oIsPay = 1
    #     dingdan.save()

        # goods = GoodsInfo.objects.filter()
    return redirect("/cars/car/")