from django.conf.urls import url

from session1 import views

urlpatterns = [
    url('test1/', views.test_cookie),
    url('test2/', views.test_cookie2),
    url('test3/', views.test_session),
    url('test4/', views.test_session2),
    url('login/', views.login),
    url('home/', views.home),

]
