from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.caso_list, name='home'),
    url(r'^caso/(?P<caso_id>\d+)$', views.caso_detail, name='detail_caso'),
]