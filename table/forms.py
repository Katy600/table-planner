from django import forms

class CreateNewGuests(forms.Form):
	add_new_guest = forms.CharField(required=True)
	add_spouse = forms.CharField(required=False, initial='None')