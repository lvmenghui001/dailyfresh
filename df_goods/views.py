from django.db.models import Q
from django.shortcuts import render, redirect,HttpResponse
from django.http import response, JsonResponse
from df_goods.models import *
from df_car.models import *
from df_user.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('gclick')[0:4]
    if request.session.get("user_id"):
        user_id = request.session["user_id"]
    else:
        user_id = 0
    count = CarInfo.objects.filter(user_id=user_id).count()
    content = {"title":'首页','guest_cart':1,
               "type0":type0,"type01":type01,
               "type1":type1,"type11":type11,
               "type2":type2,"type21":type21,
               "type3":type3,"type31":type31,
               "type4":type4,"type41":type41,
               "type5":type5,"type51":type51,
               "count":count
               }

    return render(request,"df_goods/index.html",content)

class CustomPaginator(Paginator):
    def __init__(self,current_page,per_page_num,*args,**kwargs):
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page=1
        self.per_page_num = int(per_page_num)
        super(CustomPaginator,self).__init__(*args,**kwargs)

    def pager_num_range(self):
        if self.num_pages < self.per_page_num:
            return range(1,self.num_pages+1)
        part = int(self.per_page_num/2)
        if self.current_page <= part:
            return range(1,self.per_page_num+1)
        if (self.current_page + part)>self.num_pages:
            return range(self.num_pages-self.per_page_num+1,self.num_pages+1)
        return range(self.current_page-part,self.current_page+part+1)


def list(request):
    current_page = request.GET.get("p")
    type = request.GET.get('type')
    sort = request.GET.get('sort')
    typelist = TypeInfo.objects.filter(ttitle=type).all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:3]
    if sort == "1":
        type01 = typelist[0].goodsinfo_set.order_by('-id')[0:15]
    elif sort == "2":
        type01 = typelist[0].goodsinfo_set.order_by('-gprice')[0:15]
    else:
        type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:15]
    paginator = CustomPaginator(current_page, 5, type01,10)  #paginator对象
    try:
        type01 = paginator.page(current_page)  #Page对象
    except PageNotAnInteger:
        type01 = paginator.page(1)
    except EmptyPage:
        type01 = CustomPaginator(paginator.num_pages)
    if request.session.get("user_id"):
        user_id = request.session["user_id"]
    else:
        user_id = 0
    count = CarInfo.objects.filter(user_id=user_id).count()

    content = {"type": type, "type0": type0, "type01":type01,'sort':sort,"count":count}
    return render(request, "df_goods/list.html",content)

def detail(request):

    id = request.GET.get("id")
    good = GoodsInfo.objects.get(id=id)
    good.gclick = good.gclick + 1
    good.save()

    typelist = TypeInfo.objects.filter(id = good.gtype_id).all()
    new_goods = typelist[0].goodsinfo_set.order_by('-id')[0:2]
    now_type = GoodsInfo.objects.get(id=id).gtype
    if request.session.get("user_id"):
        user_id = request.session["user_id"]
    else:
        user_id = 0
    count = CarInfo.objects.filter(user_id=user_id).count()
    content = {"good":good,"new_goods":new_goods,"count":count,"now_type":now_type}
    response = render(request, "df_goods/detail.html", content)
    # 记录最新浏览，在用户中心用
    if "user_id" in request.session:
        user_id = request.session["user_id"]
        goods_ids = UserInfo.objects.filter(id=user_id)[0].uhistory
        goods_id = '%d'%int(id)
        if goods_ids!='':#判断是否有浏览记录
            goods_ids1 = goods_ids.split(',') #拆分为列表
            if goods_ids1.count(goods_id)>=1:#如果商品是否被记录删除，被记录则删除记录
                goods_ids1.remove(goods_id)
            goods_ids1.insert(0,goods_id) #添加到第一个
            if len(goods_ids1)>=6: #如果大于5则删除最后一个
                del goods_ids1[5]
            goods_ids=','.join(goods_ids1) #拼接为字符串
        else:
            goods_ids=goods_id #没有浏览记录则直接添加
        UserInfo.objects.filter(id=user_id).update(uhistory = goods_ids)
    return response


# 搜索功能
def search(request):
    current_page = 1
    sort = 1
    cont = request.GET.get('data')
    goods = GoodsInfo.objects.filter(Q(gtitle__contains=cont)|Q(gtype__ttitle__contains=cont)).all()
    if goods:
        type0 = goods.order_by('-id')[0:3]
        if sort == "1":
            type01 = goods.order_by('-id')[0:15]
        elif sort == "2":
            type01 = goods.order_by('-gprice')[0:15]
        else:
            type01 = goods.order_by('-gclick')[0:15]
        paginator = CustomPaginator(current_page, 5, type01, 10)  # paginator对象
        try:
            type01 = paginator.page(current_page)  # Page对象
        except PageNotAnInteger:
            type01 = paginator.page(1)
        except EmptyPage:
            type01 = CustomPaginator(paginator.num_pages)
        if request.session.get("user_id"):
            user_id = request.session["user_id"]
        else:
            user_id = 0
        count = CarInfo.objects.filter(user_id=user_id).count()
        content = {"type0": type0, "type01": type01, 'sort': sort, "count": count}
        return render(request, "df_goods/search.html",content)

    else:
        data = {
            "data":"fail"
        }
        return JsonResponse(data)