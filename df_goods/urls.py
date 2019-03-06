from django.conf.urls import url
# from df_user import views
from df_goods import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^list/$', views.list),
    url(r'^detail/$', views.detail),
    url(r'^search/',views.search),
]