from django.db import models

# Create your models here.
class CarInfo(models.Model):  #谁买了几个什么
    goods = models.ForeignKey('df_goods.GoodsInfo',on_delete=models.CASCADE,verbose_name="商品")
    user = models.ForeignKey('df_user.UserInfo', on_delete=models.CASCADE,verbose_name="用户名")
    count = models.IntegerField(verbose_name="数量")
    def __str__(self):
        return self.goods

    class Meta:
        verbose_name="购物车表"
        verbose_name_plural=verbose_name
