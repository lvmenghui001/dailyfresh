from django.conf.urls import url
# from df_user import views
from . import views

urlpatterns = [
    # 注册
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exist/$',views.register_exist),

    # 登录
    url(r'^login/$',views.login),
    url(r'^login_handle/$',views.login_handle),
    url(r'^logout/$',views.logout),

    url(r'^info/$',views.info),
    url(r'^add_info/$',views.add_info),

    url(r'^order/$',views.order),
    url(r'^site/$',views.site),
    url(r'^site_del/(\d+)/$',views.site_del),

    # 省市区
    url(r'^province/$',views.province),
    url(r'^city/(\d+)/$',views.city),

    url(r'^sendCode/$',views.sendCode),
]