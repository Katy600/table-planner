from django import forms
from table.models import GuestList
from django.forms import CharField

class CreateNewGuests(forms.Form):
	add_new_guest = forms.CharField(required=True)
	add_spouse = forms.CharField(required=False, initial='None')