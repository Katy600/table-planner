from django.shortcuts import render
from django.views.generic import ListView
from table.models import GuestList
from django.template import Template
from django.template.response import TemplateResponse


def view_guest_list(request):
	return TemplateResponse(request, 'table_plan.html', {'guestlist': GuestList.objects.all()})
