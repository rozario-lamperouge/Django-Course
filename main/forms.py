from django import forms

class ContactForm(forms.Form):
	Full_Name = forms.CharField(label='Full Name',max_length=200)
	Email = forms.EmailField()
	Phone_No = forms.CharField(max_length=100)
	Message = forms.CharField(widget=forms.Textarea)