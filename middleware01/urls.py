from django.conf.urls import url

from middleware01 import views

urlpatterns = [
    url('01/', views.test)
]
