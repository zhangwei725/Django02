from django.conf.urls import url, include
from django.contrib import admin

from day06 import views

"""
文件上传功能
"""
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^day06/', include('day06.urls')),
    url(r'^form/', include('form01.urls')),
    url(r'^session1/', include('session1.urls')),

]
