from django.urls import path
from . import views as er_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ER'
urlpatterns = [
path('search/',er_views.er_home,name="search"),
path('Patient/<slug:code>',er_views.patient_info,name="patient"),

]
