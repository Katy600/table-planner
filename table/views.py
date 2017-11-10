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
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,ListView

def view_guest_list(request):
  guestlist = GuestList.objects.all()
  return TemplateResponse(request, 'table_plan.html', {'guestlist': guestlist})

def search_guests(request):
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
      return render(request, 'table/see_results.html', {'guests': guests, 'name': name})

def new_guests(request):
  error = False
  if request.method == 'POST':
    form = CreateNewGuests(request.POST)
    if form.is_valid():
      guest = form.cleaned_data['add_new_guest']
      spouse = form.cleaned_data['add_spouse']
      new_guest = request.POST['add_new_guest']
      guest_in_database = GuestList.objects.filter(first_name__icontains=new_guest)
      if guest_in_database:
        error = True
        return render(request, 'enter_guest_details.html', {'form': form, 'error': error})
      elif error == False:
        guest_entered = GuestList(first_name=guest, spouse=spouse)
        guest_entered.save()
        messages.success(request, 'A new guest %s has been added.' % guest_entered)
        return HttpResponseRedirect('/create-new-guest/completed/')
  else:
      form = CreateNewGuests()
      return render(request, 'enter_guest_details.html', {'form': form, 'error': error})

# def delete(request):
#   if 'delete_guest' in request.GET:
#    message = 'You are deleting: %r' % request.GET['delete_guest']
#    guest = request.GET['delete_guest']
#    print('guest', guest)
#    print('message', message)
#    guest_list = GuestList.objects.filter(first_name__icontains=guest).delete()
#    print(guest_list)
   # return render(request, 'table/table_plan.html', {'message': message, 'guest': guest})

def delete(request, id):
  # guest = GuestList.objects.filter(pk=pk)
  guest = get_object_or_404(GuestList, id=id)
  print("guest", guest)
  if request.method=='POST':
    # guest = GuestList.objects.filter(pk=delete_guest).delete()
    # print("guest", guest)
    guest.delete()
    # return redirect('/')
    return render(request, 'table/table_plan.html', {'guest':guest})


# def guest_edit(request, id, template_name='table/table_plan.html'):
#     guest = get_object_or_404(GuestList, id=id)
#     form = CreateNewGuests(request.POST)
#     if form.is_valid():
#         form.save()
#         # return redirect('/')
#     return render(request, template_name, {'form':form})

def guest_edit(request, id):
  guest = GuestList.objects.get(id=id)
  context = {"guest": guest}
  return render(request, 'table/edit_guest.html', context)

def update(request, id):
  guest = GuestList.objects.get(id=id)
  guest.first_name = request.POST['name']
  guest.spouse = request.POST['spouse']
  guest.save()
  return redirect('/')



  # guestlist = GuestList.objects.all()
  # if request.method == 'POST':
  #     # Fetch list of items to delete, by ID
  #     items_to_delete = request.POST.getlist('delete_items')
  #     # Delete those items all in one go
  #     GuestList.objects.filter(pk__in=items_to_delete).delete()
  # return render(request, 'table/table_plan.html', {'guestlist': guestlist, 'items_to_delete': items_to_delete})



      