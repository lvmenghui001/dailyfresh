from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20,verbose_name="用户姓名")
    upwd = models.CharField(max_length=40,verbose_name="用户密码")
    uphone = models.CharField(max_length=30,verbose_name="用户手机",default="")
    uhistory = models.CharField(max_length=200,verbose_name="历史记录",default="")

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

# default,blank是python层面的约束，不影响数据库结构
class AreaInfo(models.Model):
    title = models.CharField(max_length=20,verbose_name="名称")
    parea = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,verbose_name="上一级")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="省市区表"
        verbose_name_plural=verbose_name

class SiteInfo(models.Model):
    uname = models.CharField(max_length=50,verbose_name="收货人姓名")
    uaddress = models.CharField(max_length=100,verbose_name="收货地址")
    uyoubian = models.CharField (max_length=6, default='', verbose_name="邮编")
    uphone = models.CharField (max_length=11, default='', verbose_name="收货人手机")
    user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    isDefault = models.BooleanField(default=False,verbose_name="是否设为默认")
