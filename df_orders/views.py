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
    # t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    # print(t)
    order.odate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    order.oIsPay = 0
    order.ototal = sum([a*b for a,b in zip(sku_price,sku_counts)])
    order.oaddress = user_id
    order.user_id = user_id
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

    # 此用户此时提交的订单
    user = SiteInfo.objects.get (user=user_id, isDefault=1)
    if user:
        user = user
    else:
        user = SiteInfo.objects.filter(user=user_id).order_by("id")
        if user:
            user = user[0]
        else:
            user = ""

    # 返回订单信息
    orders = OrderDetailInfo.objects.filter(order__user_id=user_id,order__oid=str(int(time.time())))
    context={
        "ushou":user,
        "orders":orders,
    }
    return render(request, "df_order/order.html", context)


def buy(request,good_id,total_price):
    good = GoodsInfo.objects.get(good_id)
    num = total_price / good.gprice
    print(good_id,total_price,num)
    return redirect("/cars/car/")