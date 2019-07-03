from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as admins_views

app_name = 'admins'
urlpatterns = [
	path('', admins_views.admin_home, name='admins-home'),

]