from django.urls import path
from . import views as maternity_views
from django.conf.urls.static import static


app_name = 'maternity'
urlpatterns = [

path('scan/',maternity_views.scancode,name="scan"),
path('patient/<slug:code>',maternity_views.maternityPatient,name="maternityPatient"),

]
