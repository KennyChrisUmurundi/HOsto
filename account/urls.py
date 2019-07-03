from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as account_views

app_name = 'account'
urlpatterns = [
	path('', account_views.login_view, name='user-login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user-logout'),
	path('register/', account_views.UserSignUpView.as_view(), name='user-register'),
	path('user_list/', account_views.user_manage, name='user-list'),
	path('user_update/user/<int:id>', account_views.user_update, name='user-update'),
	path('UserPasswordUpdate/', account_views.user_update_password, name='user-changePassword'),	
	#path('user_manage/', account_views.user_manage, name='user-manage'),

]
