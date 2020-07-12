from django import forms
from .models import post


class postform(forms.ModelForm):
	class Meta:
		model = post
		fields = ('title', 'auther', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-group col-md-6'}),
			'auther': forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
			'body': forms.Textarea(attrs={'class': 'form-control'})

		}