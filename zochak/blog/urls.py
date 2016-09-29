from django.conf.urls import url
from .views import zocbo_list, zocbo_detail, zocbo_new

urlpatterns = [
    url(r'^list/$', zocbo_list, name="zocbo_list"),
    url(r'^list/(?P<pk>\d+)$', zocbo_detail, name="zocbo_detail"),
    url(r'^list/new/$', zocbo_new, name="zocbo_new"),
]