from django import forms
from models import Author, Publisher

class ContactForm(forms.Form):

	subject	 = forms.CharField()
	email = forms.EmailField(required=False, label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 5:
			raise forms.ValidationError("Not enough words!")
		return message

class InsertBookForm(forms.Form):

	title = forms.CharField()
	authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
	publisher = forms.ModelMultipleChoiceField(queryset=Publisher.objects.all())
	publication_date = forms.DateField()

	def clean_message(self):
		title = self.clean_data['title']
		if len(title) == 0:
			raise forms.ValidationError("Title not be empty")
		else:
			raise title