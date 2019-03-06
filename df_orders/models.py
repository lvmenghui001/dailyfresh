from django.db import models

class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True,verbose_name="订单编号")
    user = models.ForeignKey("df_user.UserInfo", on_delete=models.CASCADE,verbose_name="订单用户名")
    odate = models.DateTimeField(auto_now=True,verbose_name="订单日期")
    oIsPay = models.BooleanField(default=False,verbose_name="是否付款")
    ototal = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="订单总额")
    oaddress = models.CharField(max_length=10,verbose_name="订单地址")

    class Meta:
        verbose_name = "订单信息表"
        verbose_name_plural = verbose_name


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey("df_goods.GoodsInfo",on_delete=models.CASCADE,verbose_name="商品名")
    order = models.ForeignKey("OrderInfo",on_delete=models.CASCADE,verbose_name="订单")
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="商品单价")
    count = models.IntegerField(verbose_name="商品数量")
    total_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="总价")

    class Meta:
        verbose_name = "订单详情表"
        verbose_name_plural = verbose_name
