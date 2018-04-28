from django.conf.urls import url

from day06 import views

"""
文件上传功能
"""
urlpatterns = [
    # views.对象.as_view()
    url('^upload/', views.UploadFile.as_view()),
    url('register/', views.upload)
]
