from django.conf.urls import url
from django.views.generic import TemplateView
from table.views import Table

urlpatterns = [
	url(r'^$', Table.as_view(), name='table'),
]