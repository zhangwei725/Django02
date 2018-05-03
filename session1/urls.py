from django.conf.urls import url

from session1 import views

urlpatterns = [
    url('test1/', views.test_cookie),
    url('test2/', views.test_cookie2),

]
