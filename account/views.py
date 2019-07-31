from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import User

from account.models import Role

from . import forms as account_forms
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class UserSignUpView(CreateView):
	model = User
	form_class	=	account_forms.UserSignUpForm
	template_name =	'account/register.html'

	def form_valid(self, form):
		password = form.cleaned_data['password1']
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		print(password)
		print(username)
		print(email)

		send_mail(
			'Account Created Successfully',
			'You account has been created Successfully, Username: '+ username + ' and Password: ' + password + '. It is adviced that you change you password immediatly after logging in. Thank You. Administration.',
			'ndayikennysmuusic@gmail.com',
			[email],
			fail_silently=False
		)

		user 	=	form.save()

		#messages.success(request, 'Account Created Successfully!')
		return redirect('account:user-list')


def login_view(request):
	if request.method == 'POST':
		form = account_forms.LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data.get('username')
			p = form.cleaned_data.get('password')
			user = authenticate(username=u, password=p)
			if user is not None and user.role.role == 'is_doctor' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('doctor:ScanCode'))
			elif user is not None and user.role.role == 'is_receptionist' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('reception:reception-home'))
			elif user is not None and user.role.role == 'is_labTech' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('Laboratory:scanBarcode'))
			elif user is not None and user.role.role == 'is_pharmacist' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('pharmacy:scanBarcode'))

			elif user is not None and user.role.role == 'is_nurse' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('icu:ScanCode'))

			elif user is not None and user.role.role == 'is_admin' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('admins:admins-home'))

			elif user is not None and user.role.role == 'is_mortury_attendant' and user.role.status == 'active':
				login(request, user)
				return HttpResponseRedirect(reverse('mortury:scan'))

			elif user is not None and user.role.role == 'is_doctor' and user.role.status == 'revoked':
				messages.error(request, 'Access Revoked! Contact System Admin.')
				return render(request, 'account/login.html', {'form': form})
			elif user is not None and user.role.role == 'is_receptionist' and user.role.status == 'revoked':
				messages.error(request, 'Access Revoked! Contact System Admin.')
				return render(request, 'account/login.html', {'form': form})
			elif user is not None and user.role.role == 'is_labTech' and user.role.status == 'revoked':
				messages.error(request, 'Access Revoked! Contact System Admin.')
				return render(request, 'account/login.html', {'form': form})
			elif user is not None and user.role.role == 'is_admin' and user.role.status == 'revoked':
				messages.info(request, 'Access Revoked! Contact System Admin.')
				return render(request, 'account/login.html', {'form': form})
			else:
				messages.warning(request, 'Username or Password Incorrect!')
				return render(request, 'account/login.html', {'form': form})

		else:
			messages.warning(request, 'Username or Password Incorrect!')
			return render(request, 'account/login.html', {'form' : form})

	else:
		return render(request, 'account/login.html', {'form' : account_forms.LoginForm})

#AJAX Validation Username
def validate_username(request):
	username = request.GET.get('username', None)
	data = {
		'is_taken':	CustomUser.objects.filter(username__iexact=username).exists()
	}
	if data['is_taken']:
		data['error-message'] = 'A user with this username already exists'
	return JsonResponse(data)

@login_required(login_url='/account/login')
def logout_user(request):
    logout(request)
    # Redirect to index page
    return HttpResponseRedirect(reverse('account:user-login'))

def user_manage(request):

	context = {
		'users':	User.objects.all().order_by('-date_joined'),
	}

	return render(request, 'account/user_manage.html', context)


@login_required(login_url='/account/login')
def user_update(request, id):

	instance = get_object_or_404(User, id=id)
	u_form = account_forms.UserUpdateForm(request.POST or None, instance=instance )
	r_form = account_forms.RoleUpdateForm(request.POST or None, instance=instance.role)
	if u_form.is_valid() and r_form.is_valid():
		u_form.save()
		r_form.save()
		messages.success(request, f'Update Success')
		return redirect('account:user-list')
	else:
		u_form = account_forms.UserUpdateForm(instance=instance)
		r_form = account_forms.RoleUpdateForm(instance=instance.role)

	context = {

		'u_form': u_form,
		'r_form': r_form,


	}

	return render(request, 'account/user_update_form.html', context)


@login_required(login_url='/')
def user_update_password(request):

	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, form.user) #very import
			messages.success(request, 'Your Password was Successfully Updated')
			if user.role.role == 'is_admin':
				return redirect('admins:admins-home')
			elif user.role.role == 'is_doctor':
				return redirect('doctor:ScanCode')
			if user.role.role == 'is_receptionist':
				return redirect('reception:reception-home')
			if user.role.role == 'is_labTech':
				return redirect('lab:lab-home')
		else:
			messages.error(request, 'Please Correct the Error bellow')

	else:
		form = PasswordChangeForm(user=request.user)

	context = {
		'form': form,
	}

	return render(request, 'account/password_user_update_form.html', context)

	# instance = get_object_or_404(User, id=id)
	# update_pass_form = account_forms.PasswordUserUpdateForm(request.POST or None, instance=instance )

	# if update_pass_form.is_valid():
	# 	update_pass_form.save()
	# 	messages.success(request, f'Update Success')
	# 	return redirect('account:admins-home')
	# else:
	# 	update_pass_form = account_forms.PasswordUserUpdateForm(instance=instance)

	# context = {

	# 	'update_pass_form': update_pass_form,


	# }

	# return render(request, 'account/password_user_update_form.html', context)



#class UserDetailView(DetailView):
#	model = User
#	template_name = 'account/user_detail.html'
#	#form_class = tasks_forms.TaskDetailForm
#	#queryset = StatusType.objects.all()
#
#	def get_context_data(self, **kwargs):
#		context = super(UserDetailView, self).get_context_data(**kwargs)
#		context['user_role'] = Role.objects.filter(user=self.kwargs.get('pk'))
#		#context['task_status'] = StatusType.objects.filter(tasks=self.kwargs.get('pk')).first()
#		#context['categories'] = Category.objects.filter(question=self.kwargs.get('pk'))
#		return context
