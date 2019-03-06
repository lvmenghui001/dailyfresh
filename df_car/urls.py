from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^car/$',views.car),
    url(r'^add/_(\d+)_(\d+)/$',views.add),
    url(r'^edit/(\d+)/(\d+)/$',views.edit),
    url(r'^car_del/(\d+)/$',views.car_del),
]