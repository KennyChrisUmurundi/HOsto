from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Role

class LoginForm(forms.Form):

	username	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'username',
																	'class'			:	'form-control',
																	'type'			:	'text',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter Username',
																	'tabindex'		:	'3',
																	}))
	password	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'password',
																	'class'			:	'form-control',
																	'type'			:	'password',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter password',
																	'tabindex'		:	'5',
																	}))


class UserSignUpForm(UserCreationForm):

	username	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'username',
																	'class'			:	'form-control',
																	'type'			:	'text',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter Username',
																	'tabindex'		:	'3',
																	}))

	first_name	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'first_name',
																	'class'			:	'form-control',
																	'type'			:	'text',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter Staff Firstname',
																	'tabindex'		:	'1',
																	}))

	last_name	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'last_name',
																	'class'			:	'form-control',
																	'type'			:	'text',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter Staff Lastname',
																	'tabindex'		:	'2',
																	}))

	email	=	forms.CharField(max_length=60,
									widget=forms.TextInput(attrs={	'name'			:	'email',
																	'class'			:	'form-control',
																	'type'			:	'email',
																	'autocomplete'	:	'on',
																	'placeholder'	:	'Enter Staff Email Address',
																	'tabindex'		:	'4',
																	}))

	password1	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'password1',
																	'class'			:	'form-control gen',
																	'type'			:	'password',
																	'autocomplete'	:	'off',
																	'placeholder'	:	'Enter Password',
																	'tabindex'		:	'5',
																	'readonly'		:	'true',
																	}))

	password2	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'password2',
																	'class'			:	'form-control pass',
																	'type'			:	'password',
																	'autocomplete'	:	'off',
																	'placeholder'	:	'Confirm Password',
																	'tabindex'		:	'6',
																	'readonly'		:	'true',
																	}))

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username =	self.cleaned_data.get('username')

		if User.objects.filter(email=email).exclude(username=username):
			raise forms.ValidationError(u'Email Addresses must be unique.')
		return email

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if not password1 or not password2:
			raise ValidationError("Passwords must not be Empty")

		if password1 != password2:
			raise ValidationError("Passwords do not match")


class PasswordUserUpdateForm(forms.ModelForm):
	# username	=	forms.CharField(max_length=100,
	# 								widget=forms.TextInput(attrs={	'name'			:	'username',
	# 																'type'			:	'text',
	# 																'readonly'		:	'True'
	# 																}))
	# email = forms.EmailField(max_length=300,
	# 								widget=forms.TextInput(attrs={	'name'			:	'email',
	# 																'type'			:	'email',
	# 																'readonly'		:	'True'
	# 																}))
	password	=	forms.CharField(max_length=30,
									widget=forms.TextInput(attrs={	'name'			:	'password1',
																	'class'			:	'form-control',
																	'type'			:	'password',
																	'autocomplete'	:	'off',
																	'placeholder'	:	'Enter Password',
																	'tabindex'		:	'5',
																	}))
	class Meta:
		model = User
		fields = ['password']

class UserUpdateForm(forms.ModelForm):
	username	=	forms.CharField(max_length=100,
									widget=forms.TextInput(attrs={	'name'			:	'username',
																	'type'			:	'text',
																	'readonly'		:	'True'
																	}))
	email = forms.EmailField(max_length=300,
									widget=forms.TextInput(attrs={	'name'			:	'email',
																	'type'			:	'email',
																	'readonly'		:	'True'
																	}))
	class Meta:
		model = User
		fields = ['username', 'email']



class RoleUpdateForm(forms.ModelForm):

	role = forms.ChoiceField(choices=[('', 'Select User Role'),
									  ('is_admin', 'Administrator'),
									  ('is_doctor', 'Doctor'),
									  ('is_labTech', 'Lab Technician'),
									  ('is_receptionist', 'Receptionist')],
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'role', }))

	status = forms.ChoiceField(choices=[('', 'Select User Status'),
									  ('revoked', 'Revoked'),
									  ('active', 'Active'),],
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'status', }))
	class Meta:
		model = Role 
		fields = ['role', 'status']