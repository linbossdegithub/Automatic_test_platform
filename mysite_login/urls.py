"""mysite_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from login import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^blog/', views.blog),
    url(r'^blogshow/', views.blogshow),
    url(r'^auto_test/', views.auto_test),
    url(r'^auto_testshow/', views.auto_testshow),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha', include('captcha.urls')),
    #url(r'^pic_handle/$', views.pic_handle),
    #url(r'^pic_show/$', views.pic_show),
    url(r'do_add/$', views.do_add),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^download_file/$',views.download_file),
    url(r'^download_fileshow/$',views.download_fileshow),
    url(r'^upload/$',views.upload),
    url(r'^baidumap/$',views.baidumap),
    url(r'^jietu/$',views.jietu),

    ]
