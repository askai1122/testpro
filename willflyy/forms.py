from django.core import validators
from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo


def passworderror(value):
	min_length = 9

	if len(value) < min_length:
		raise forms.ValidationError('Password Must Be At Least 9 Characters Long')
	if not any(char.isdigit() for char in value):
		raise forms.ValidationError('Password must contain at least 1 Number')
	if not any(char.isalpha() for char in value):
		raise forms.ValidationError('Password must contain at least one Letter')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():

		model = User
		fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('picture',)
# def passwordError(value):
# 	if value[0].lower() != 'z':
# 		raise forms.ValidationError("Pass Needs To Start with Char, Num")






class FormName(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}))

	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	# varify_email = forms.EmailField()



	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), validators=[passworderror])
	uploadprofile = forms.ImageField(required=False)
	# passwordagain = forms.CharField(widget=forms.PasswordInput,validators=[passwordError])

	def clean(self):


		botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


