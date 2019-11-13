from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as icu_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'icu'
urlpatterns = [
path('Medical Update/',icu_views.update_list,name="add-medical"),
path('scan/',icu_views.ScanCode,name="ScanCode"),
path('patient/<slug:code>',icu_views.patient,name="patient"),
path('feedback/<slug:code>/<int:id>',icu_views.feedback,name="feedback"),
]
