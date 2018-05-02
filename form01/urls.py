from django.conf.urls import url

from form01 import views

urlpatterns = [
    # url(r'test/', views.test, name='test'),
    url(r'register/', views.register, name='register'),
]
