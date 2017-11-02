from django.shortcuts import render
from django.views.generic import ListView
from table.models import GuestList
from django.template import Template
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime
from table.forms import CreateNewGuests
from django.core import validators
from django import forms


def view_guest_list(request):
	guestlist = GuestList.objects.all()
	# return render(request, 'table/table_plan.html')
	return TemplateResponse(request, 'table_plan.html', {'guestlist': GuestList.objects.all()})

def search_guests(request):
	# return render(request, 'table/search_guests.html')
	
	return TemplateResponse(request, 'search_guests.html', {'guestlist': GuestList.objects.all()})

def search(request):
	errors = []
	if 'name' in request.GET:
		name = request.GET['name']
		if not name:
			errors.append('Enter a guests name.')
			return render( request, 'table/search_guests.html', {'errors' : errors})
		elif len(name) > 20:
			errors.append('Please enter at most 20 characters.')
			return render( request, 'table/search_guests.html', {'errors' : errors})
		else:
			guests = GuestList.objects.filter(first_name__icontains=name)
			return render(request, 'table/see_results.html',
						{'guests': guests, 'name': name})

def new_guests(request):
	if request.method == 'POST':
		form = CreateNewGuests(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cd['add_new_guest'],
			cd['add_spouse']
			
				
		return HttpResponseRedirect('/create-new-guest/completed/')
	else:
			form = CreateNewGuests()

			return render(request, 'enter_guest_details.html', {'form': form})


			