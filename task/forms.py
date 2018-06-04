from django import forms

class todoForm(forms.Form):
	text = forms.CharField(max_length=30,
		widget=forms.TextInput(
			attrs={'name':'event', 'placeholder':'enter a task', 'class':'task'}))