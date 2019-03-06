"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from df_goods import views as views1

urlpatterns = [
    url(r'^$',views1.index),
    url(r'^admin/',admin.site.urls),
    url(r'^user/', include('df_user.urls')),
    url(r'^goods/',include('df_goods.urls')),
    url(r'^cars/',include('df_car.urls')),
    url(r'^orders/', include('df_orders.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
    # url(r'^search/', include('haystack.urls')),

]
