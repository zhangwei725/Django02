from django.conf.urls import url

from auth01 import views

urlpatterns = [
    url('yz/', views.yanzhen, name='yz'),
    url('register/', views.register, name='reg'),
    url('verify/', views.get_verify_code, name='verify')
]
