from django.db import models
from tinymce.models import HTMLField
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20,verbose_name="商品类名")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除")
    def __str__(self):
        return self.ttitle
    class Meta:
        verbose_name="商品类型表"
        verbose_name_plural = verbose_name

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20,verbose_name="商品名")
    gpic = models.ImageField(upload_to="goods",verbose_name="商品图片")
    gprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="商品价格")
    isDelete = models.BooleanField(default=False,verbose_name="是否删除")
    gunit = models.CharField(max_length=20,default="500g",verbose_name="规格")
    gclick = models.IntegerField(verbose_name="点击量")
    gjianjie = models.CharField(max_length=200,verbose_name="商品简介")
    gkucun = models.IntegerField(verbose_name="库存")
    gcontent = HTMLField(verbose_name="商品详情")
    gtype = models.ForeignKey("TypeInfo",on_delete=models.CASCADE,verbose_name="商品类型")

    class Meta:
        verbose_name="商品表"
        verbose_name_plural = verbose_name



