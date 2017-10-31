from django.shortcuts import render
from django.views.generic import ListView
from table.models import GuestList
from django.template import Template
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import render


def view_guest_list(request):
	guestlist = GuestList.objects.all()
	# return render(request, 'table/table_plan.html')
	return TemplateResponse(request, 'table_plan.html', {'guestlist': GuestList.objects.all()})

def search_guests(request):
	# return render(request, 'table/search_guests.html')
	
	return TemplateResponse(request, 'search_guests.html', {'guestlist': GuestList.objects.all()})

def search(request):
	error = False
	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			error = True
			return render( request, 'table/search_guests.html', {'error' : error})
		else:
			guests = GuestList.objects.filter(first_name__icontains=name)
			return render(request, 'table/see_results.html',
						{'guests': guests, 'name': name})

			