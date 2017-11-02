from django.conf import settings
from django.conf.urls import url
from django.views.generic import ListView
from table.views import view_guest_list
from . import views

urlpatterns = [
	url(r'^$', view_guest_list, name='guest_list'),
	url(r'^search-guests/$', views.search_guests, name='search_guests'),
	url(r'^search/$', views.search),
	url(r'^create-new-guest/$', views.new_guests, name='new_guest'),
	url(r'^create-new-guest/completed/$', views.new_guests, name='completed'),
]

# if settings.DEBUG:
# 	urlpatterns += [url(r'debuginfo/$', views.debug),]