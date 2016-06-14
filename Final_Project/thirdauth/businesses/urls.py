from django.conf.urls import patterns, url
from businesses import views

urlpatterns = patterns('',
    url(r'^(?P<business_id>\d+)/$', views.menu, name='menu'),
    url(r'^(?P<business_id>\d+)/goal/$', views.goal, name='goal'),
    url(r'^(?P<business_id>\d+)/worker/$', views.worker, name='worker'),
    url(r'^(?P<business_id>\d+)/finance/$', views.finance, name='finance'),
    url(r'^(?P<business_id>\d+)/resource/$', views.resource, name='resource'),
    url(r'^(?P<business_id>\d+)/resource/location/(?P<location_id>\d+)$', views.room, name='room'),
    url(r'^(?P<business_id>\d+)/resource/location/(?P<location_id>\d+)/reservation/(?P<room_id>\d+)$', views.reservation, name='reservation'),
    url(r'^(?P<business_id>\d+)/resource/location/(?P<location_id>\d+)/return/(?P<room_id>\d+)$', views.room_return, name='room_return'),
    url(r'^(?P<business_id>\d+)/resource/location/$', views.location, name='location'),
    url(r'^(?P<business_id>\d+)/resource/material/$', views.material, name='material'),
    url(r'^(?P<business_id>\d+)/resource/material/number/(?P<material_id>\d+)$', views.material_number, name='material_number'),
    url(r'^(?P<business_id>\d+)/resource/material/return/(?P<material_id>\d+)$', views.material_return, name='material_return'),
    url(r'^(?P<business_id>\d+)/goal/(?P<goal_id>\d+)/goal_chart$', views.goal_chart_view, name='goal_chart'),
    url(r'^(?P<business_id>\d+)/finance/(?P<finance_id>\d+)/finance_chart$', views.finance_chart_view, name='finance_chart'),
)
