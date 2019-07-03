from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def admin_home(request):

	context = {
		'users':	User.objects.all().order_by('-date_joined'),
	}

	return render(request, 'account/user_manage.html', context)
