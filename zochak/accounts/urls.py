from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import signup


urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, {'next_page': 'index'}, name="logout"),
    url(r'^signup/$', signup, name="signup"),
]
