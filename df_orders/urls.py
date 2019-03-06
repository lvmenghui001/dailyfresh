from django.conf.urls import url
from df_orders import views

urlpatterns = [
    url(r'^pay/$', views.pay),
    url(r'^buy/(\d+)/(\.\d+)?/$', views.buy),
    url(r'^buy/(\d+)/(\.\d+)?/$', views.buy),
]